# Base Container

This container includes

* PyTorch
* TensorFlow
* Jupyter Lab
* JetBot Python API

Among other small related dependencies.

```bash
cd docker/base
./build.sh
```

Other containers depend on this, it's typically not run directly.  You could 
build your own container on top of this.
