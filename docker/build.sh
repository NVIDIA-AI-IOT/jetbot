BASE_IMAGE=$1

# find L4T_VERSION
source ../scripts/l4t-version.sh

if [ -z $BASE_IMAGE ]; then
	if [ $L4T_VERSION = "32.4.4" ]; then
		BASE_IMAGE="nvcr.io/nvidia/l4t-pytorch:r32.4.4-pth1.6-py3"
	else
		echo "cannot build jetbot docker containers for L4T R$L4T_VERSION"
		echo "please upgrade to the latest JetPack, or build jetson-inference natively"
		exit 1
	fi
fi

echo "cd base && ./build.sh $BASE_IMAGE && cd .."
cd base && ./build.sh $BASE_IMAGE && cd ..

echo "cd models && ./build.sh && cd .."
cd models && ./build.sh && cd ..
cd display && ./build.sh && cd ..
cd jupyter && ./build.sh && cd ..
cd camera && ./build.sh && cd ..
