# Software Setup (Docker)

This page details how to set up JetBot using the pre-built JetBot docker containers. This is the best option if you want to use JetBot with an existing Jetson Nano SD card image.

???+ note
    Please note, the JetBot containers described in this page currently target a Jetson Nano SD card image flashed with JetPack 4.4. These containers will not work with other version of JetPack.

## Step 1. Setup Jetson Nano

If you haven't already, go through the initial setup of Jetson Nano.<br>
You can use your existing Jetson Nano set up (microSD card), as long as you have enough storage space left.

???+ hint
    For this, we'll assume you've set up your Jetson Nano using the **online Getting Started guide**.
        
     - [Getting Started With Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

## Step 2. Connect to Wi-Fi

If you haven't already, connect your Jetson Nano to your Wi-Fi network.

Follow this [Wi-Fi setup](wifi_setup.md) guide.


## Step 3 - Clone JetBot repo

Clone the [official JetBot GitHub repo](https://github.com/NVIDIA-AI-IOT/jetbot).

```bash
git clone http://github.com/NVIDIA-AI-IOT/jetbot.git
```

## Step 4 - Configure System

First, call the [``scripts/configure_jetson.sh``](https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/scripts/configure_jetson.sh) script to configure the power mode and other parameters.

```bash
cd jetbot
./scripts/configure_jetson.sh
```

???+ hint
    `configure_jetson.sh` also disables the GUI for the interest of saving system memory (DRAM) consumption.<br>
    If you want to re-enable the GUI, you can execute the following command.
    
    ```bash
    sudo systemctl set-default graphical.target
    ```
    
    Optionally, you can execute this script (`./scripts/re_enable_gui.sh`). 

Next, source the [``docker/configure.sh``](https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/docker/configure.sh) script to configure various environment variables related to JetBot docker.

```bash
cd docker
source configure.sh
```

Finally, if you haven't already, set the default docker runtime to NVIDIA using [``docker/set_nvidia_runtime.sh``](https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/docker/set_nvidia_runtime.sh).  This is needed to use
CUDA related components with the containers.

```bash
./set_nvidia_runtime.sh
```

If needed, you can also set memory limits on the Jupyter container.

```bash
export JETBOT_JUPYTER_MEMORY=500m
export JETBOT_JUPYTER_MEMORY_SWAP=3G
```


## Step 5 - Enable all containers

Call the following to enable the JetBot docker containers 

```bash
sudo systemctl enable docker   # enable docker daemon at boot
./enable.sh $HOME   # we'll use home directory as working directory, set this as you please.
```

Now you can go to ``https://<jetbot_ip>:8888`` from a web browser and start programming JetBot!

You can do this from any machine on your local network.  The password to log in is ``jetbot``.

![](https://user-images.githubusercontent.com/25759564/92091965-51ae4f00-ed86-11ea-93d5-09d291ccfa95.png)

The `enable.sh` script causes the docker containers to restart at boot. This means the next time you power on your JetBot, the containers will automatically start, and you should see the IP address displayed on the PiOLED display screen. All you need to do is type this into your web browser and start programming!

???+ tip
    For more information on configuring and using docker with JetBot, check out the [Docker Tips](reference/docker_tips.md) page.
    
Now that you've finished setting up you're JetBot, you're ready to run through the [examples](examples/basic_motion.md)!

