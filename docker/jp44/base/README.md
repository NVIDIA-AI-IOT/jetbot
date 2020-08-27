Base container contains software dependencies including

* PyTorch
* TensorFlow
* Jupyter Lab + Widgets

It does not contain any environment setup, like launching services for jetbot display, jupyter server, etc.

## Build

```bash
cd jetbot/docker/jp44/base
./build.sh
```

## Run

```bash
cd jetbot/docker/jp44/base
./run.sh <workspace_dir>
```
