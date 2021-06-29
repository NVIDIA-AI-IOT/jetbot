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
cd docker
source configure.sh
./build.sh
```

### Rebuilding Containers

1. To rebuild the containers make sure to disable any running containers first. *(Don't forget to move to the `docker` folder)*
    ```bash
    cd docker
    ./disable.sh
    ```
2. Rebuild the containers from scratch.
    ```bash
    source configure.sh
    ./build.sh
    ```
3. Enable the new containers with `home` as the working directory *(feel free to change)*.
    ```bash
    ./enable.sh $HOME
    ```

Users can check if the containers are running using either of the following commands:

- `sudo docker ps`
- `sudo ps -aF`

User should see both the jupyter notebook and display (stats) service running. If they are not running, try the following:

- Restarting the Jetson or
- Re-enabling the containers:
    1. Run the `disable.sh` script
    2. Followed by the `enable.sh` script