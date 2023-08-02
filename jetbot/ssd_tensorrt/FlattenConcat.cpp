#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>

#include <cublas_v2.h>

#include "NvInferPlugin.h"
#include "NvUffParser.h"

// Macro for calling GPU functions
#define CHECK(status)                             \
    do                                            \
    {                                             \
        auto ret = (status);                      \
        if (ret != 0)                             \
        {                                         \
            std::cout << "Cuda failure: " << ret; \
            abort();                              \
        }                                         \
    } while (0)

using namespace nvinfer1;

namespace
{
const char* FLATTENCONCAT_PLUGIN_VERSION{"1"};
const char* FLATTENCONCAT_PLUGIN_NAME{"FlattenConcat_TRT_jetbot"};
}

// Flattens all input tensors and concats their flattened version together
// along the major non-batch dimension, i.e axis = 1
class FlattenConcat : public IPluginV2
{
public:
    // Ordinary ctor, plugin not yet configured for particular inputs/output
    FlattenConcat() {}

    // Ctor for clone()
    FlattenConcat(const int* flattenedInputSize, int numInputs, int flattenedOutputSize)
        : mFlattenedOutputSize(flattenedOutputSize)
    {
        for (int i = 0; i < numInputs; ++i)
            mFlattenedInputSize.push_back(flattenedInputSize[i]);
    }

    // Ctor for loading from serialized byte array
    FlattenConcat(const void* data, size_t length)
    {
        const char* d = reinterpret_cast<const char*>(data);
        const char* a = d;

        size_t numInputs = read<size_t>(d);
        for (size_t i = 0; i < numInputs; ++i)
        {
            mFlattenedInputSize.push_back(read<int>(d));
        }
        mFlattenedOutputSize = read<int>(d);

        assert(d == a + length);
    }

    int32_t getNbOutputs() const noexcept
    {
        // We always return one output
        return 1;
    }

    Dims getOutputDimensions(int index, const Dims* inputs, int nbInputDims) noexcept
    {
        // At least one input
        assert(nbInputDims >= 1);
        // We only have one output, so it doesn't
        // make sense to check index != 0
        assert(index == 0);

        size_t flattenedOutputSize = 0;
        int inputVolume = 0;

        for (int i = 0; i < nbInputDims; ++i)
        {
            // We only support NCHW. And inputs Dims are without batch num.
            assert(inputs[i].nbDims == 3);

            inputVolume = inputs[i].d[0] * inputs[i].d[1] * inputs[i].d[2];
            flattenedOutputSize += inputVolume;
        }

    // return DimsCHW(flattenedOutputSize, 1, 1);
        return Dims3(flattenedOutputSize, 1, 1);
    }

    int initialize() noexcept
    {
        // Called on engine initialization, we initialize cuBLAS library here,
        // since we'll be using it for inference
        CHECK(cublasCreate(&mCublas));
        return 0;
    }

    void terminate() noexcept
    {
        // Called on engine destruction, we destroy cuBLAS data structures,
        // which were created in initialize()
        CHECK(cublasDestroy(mCublas));
    }

    size_t getWorkspaceSize(int maxBatchSize) const noexcept
    {
        // The operation is done in place, it doesn't use GPU memory
        return 0;
    }
    
    int32_t enqueue(int32_t batchSize, void const* const* inputs, void* const* outputs, void*, cudaStream_t stream) noexcept
    {
        // Does the actual concat of inputs, which is just
        // copying all inputs bytes to output byte array
        size_t inputOffset = 0;
        float* output = reinterpret_cast<float*>(outputs[0]);

        for (size_t i = 0; i < mFlattenedInputSize.size(); ++i)
        {
            const float* input = reinterpret_cast<const float*>(inputs[i]);
            for (int batchIdx = 0; batchIdx < batchSize; ++batchIdx)
            {
                CHECK(cublasScopy(mCublas, mFlattenedInputSize[i],
                                  input + batchIdx * mFlattenedInputSize[i], 1,
                                  output + (batchIdx * mFlattenedOutputSize + inputOffset), 1));
            }
            inputOffset += mFlattenedInputSize[i];
        }

        return 0;
    }

    size_t getSerializationSize() const noexcept
    {
        // Returns FlattenConcat plugin serialization size
        size_t size = sizeof(mFlattenedInputSize[0]) * mFlattenedInputSize.size()
            + sizeof(mFlattenedOutputSize)
            + sizeof(size_t); // For serializing mFlattenedInputSize vector size
        return size;
    }

    void serialize(void* buffer) const noexcept
    {
        // Serializes FlattenConcat plugin into byte array

        // Cast buffer to char* and save its beginning to a,
        // (since value of d will be changed during write)
        char* d = reinterpret_cast<char*>(buffer);
        char* a = d;

        size_t numInputs = mFlattenedInputSize.size();

        // Write FlattenConcat fields into buffer
        write(d, numInputs);
        for (size_t i = 0; i < numInputs; ++i)
        {
            write(d, mFlattenedInputSize[i]);
        }
        write(d, mFlattenedOutputSize);

        // Sanity check - checks if d is offset
        // from a by exactly the size of serialized plugin
        assert(d == a + getSerializationSize());
    }

    void configureWithFormat(const Dims* inputs, int nbInputs, const Dims* outputDims, int nbOutputs, nvinfer1::DataType type, nvinfer1::PluginFormat format, int maxBatchSize) noexcept
    {
        // We only support one output
        assert(nbOutputs == 1);

        // Reset plugin private data structures
        mFlattenedInputSize.clear();
        mFlattenedOutputSize = 0;

        // For each input we save its size, we also validate it
        for (int i = 0; i < nbInputs; ++i)
        {
            int inputVolume = 0;

            // We only support NCHW. And inputs Dims are without batch num.
            assert(inputs[i].nbDims == 3);

            // All inputs dimensions along non concat axis should be same
            for (size_t dim = 1; dim < 3; dim++)
            {
                assert(inputs[i].d[dim] == inputs[0].d[dim]);
            }

            // Size of flattened input
            inputVolume = inputs[i].d[0] * inputs[i].d[1] * inputs[i].d[2];
            mFlattenedInputSize.push_back(inputVolume);
            mFlattenedOutputSize += mFlattenedInputSize[i];
        }
    }

    bool supportsFormat(DataType type, PluginFormat format) const noexcept
    {
        return (type == DataType::kFLOAT && (format == TensorFormat::kLINEAR ||
                                             format == TensorFormat::kCHW2 ||
                                             format == TensorFormat::kHWC8 ||
                                             format == TensorFormat::kCHW4 ||
                                             format == TensorFormat::kCHW16 ||
                                             format == TensorFormat::kCHW32 || 
                                             format == TensorFormat::kDHWC8 ||
                                             format == TensorFormat::kCDHW32 ||
                                             format == TensorFormat::kHWC ||
                                             format == TensorFormat::kDLA_LINEAR ||
                                             format == TensorFormat::kDLA_HWC4 ||
                                             format == TensorFormat::kHWC16)); 
    }

    const char* getPluginType() const noexcept { return FLATTENCONCAT_PLUGIN_NAME; }

    const char* getPluginVersion() const noexcept { return FLATTENCONCAT_PLUGIN_VERSION; }

    void destroy() noexcept {}

    IPluginV2* clone() const noexcept
    {
        return new FlattenConcat(mFlattenedInputSize.data(), mFlattenedInputSize.size(), mFlattenedOutputSize);
    }

    void setPluginNamespace(const char* pluginNamespace) noexcept
    {
        mPluginNamespace = pluginNamespace;
    }

    const char* getPluginNamespace() const noexcept
    {
        return mPluginNamespace.c_str();
    }

private:
    template <typename T>
    void write(char*& buffer, const T& val) const
    {
        *reinterpret_cast<T*>(buffer) = val;
        buffer += sizeof(T);
    }

    template <typename T>
    T read(const char*& buffer)
    {
        T val = *reinterpret_cast<const T*>(buffer);
        buffer += sizeof(T);
        return val;
    }

    // Number of elements in each plugin input, flattened
    std::vector<int> mFlattenedInputSize;
    // Number of elements in output, flattened
    int mFlattenedOutputSize{0};
    // cuBLAS library handle
    cublasHandle_t mCublas;
    // We're not using TensorRT namespaces in
    // this sample, so it's just an empty string
    std::string mPluginNamespace = "";
};

// PluginCreator boilerplate code for FlattenConcat plugin
class FlattenConcatPluginCreator : public IPluginCreator
{
public:
    FlattenConcatPluginCreator()
    {
        mFC.nbFields = 0;
        mFC.fields = 0;
    }

    ~FlattenConcatPluginCreator() {}

    const char* getPluginName() const noexcept { return FLATTENCONCAT_PLUGIN_NAME; }

    const char* getPluginVersion() const noexcept { return FLATTENCONCAT_PLUGIN_VERSION; }

    const PluginFieldCollection* getFieldNames() noexcept { return &mFC; }

    IPluginV2* createPlugin(const char* name, const PluginFieldCollection* fc) noexcept
    {
        return new FlattenConcat();
    }

    IPluginV2* deserializePlugin(const char* name, const void* serialData, size_t serialLength) noexcept
    {

        return new FlattenConcat(serialData, serialLength);
    }

    void setPluginNamespace(const char* pluginNamespace) noexcept
    {
        mPluginNamespace = pluginNamespace;
    }

    const char* getPluginNamespace() const noexcept
    {
        return mPluginNamespace.c_str();
    }

private:
    static PluginFieldCollection mFC;
    static std::vector<PluginField> mPluginAttributes;
    std::string mPluginNamespace = "";
};

PluginFieldCollection FlattenConcatPluginCreator::mFC{};
std::vector<PluginField> FlattenConcatPluginCreator::mPluginAttributes;

REGISTER_TENSORRT_PLUGIN(FlattenConcatPluginCreator);
