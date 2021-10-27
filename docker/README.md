# JetBot Docker

This directory contains scripts to build the JetBot docker containers.  

## Quick Start

### Step 1 - Configure System

First, call the ``scripts/configure_jetson.sh`` script to configure the power mode and other parameters.

```bash
cd jetbot
./scripts/configure_jetson.sh
```

Next, source the ``docker/configure.sh`` script to configure various environment variables related to JetBot docker.

```bash
cd docker
source configure.sh
```

Depending on your Jetson L4T version, you may get a similar warning :

```bash
JETBOT_BASE_IMAGE not found for 32.6.1.  Please manually set the JETBOT_BASE_IMAGE environment variable. (ie: export JETBOT_BASE_IMAGE=...)
```

In the case of ``32.6.1``, the following container will work :

```bash
export JETBOT_BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3
```

Refer to ``https://ngc.nvidia.com/catalog/containers/nvidia:l4t-pytorch`` for more details.

Finally, if you haven't already, set the default docker runtime to NVIDIA.  This is needed to use
CUDA related components with the containers.

```bash
./set_nvidia_runtime.sh
```

If needed, you can also set memory limits on the Jupyter container.

```bash
export JETBOT_JUPYTER_MEMORY=500m
export JETBOT_JUPYTER_MEMORY_SWAP=3G
```

### Step 2 - Building Containers

If you want to build the containers from scratch, simply call :

```bash
./build.sh
```

### Step 3 - Enable All Containers

Call the following to enable the JetBot docker containers 

```bash
sudo systemctl enable docker   # enable docker daemon at boot
./enable.sh $HOME   # we'll use home directory as working directory, set this as you please.
```

Now you can go to ``https://<jetbot_ip>:8888`` from a web browser and start programming JetBot!
You can do this from any machine on your local network.  The password to log in is ``jetbot``.

![](https://user-images.githubusercontent.com/25759564/92091965-51ae4f00-ed86-11ea-93d5-09d291ccfa95.png)


> Note: The directory you specify to ``./enable.sh`` will be mounted as a volume in the jupyter container 
at the location ``/workspace``.  This means the work you in the ``/workspace`` folder inside container
is saved.  This is set to the root directory of Jupyter Lab.  Please note, if you work outside of that directory it will be lost when the container shuts down.
