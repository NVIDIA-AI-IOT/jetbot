# Docker

Since the release of JetPack 4.4, NVIDIA Jetson has supported [Cloud-Native](https://developer.nvidia.com/embedded/jetson-cloud-native) development. This makes it easy to develop Docker containers which package software along with it's dependencies.  This containerization ensures that no-matter your system setup, it's easy to install and run software in a reproducible way.  

We've included containers which package JetBot and it's various dependencies.  Compared to our previous method of releasing JetBot as a large SD card image, this makes it much easier to install JetBot
on your existing Jetson system.  Rather than downloading an entirely new SD card image, you just run a command to launch the docker containers and turn your Jetson Nano into a JetBot.

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

### Step 2 - Enable all containers

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

## Building Containers

If you want to build the containers from scratch, simply call

```bash
./build.sh
```
