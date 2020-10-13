# Software Setup (Docker)

This page details how to set up JetBot using the pre-built JetBot docker containers. This is the best option if you want to use JetBot with an existing Jetson Nano SD card image.

???+ note
    Please note, the JetBot containers described in this page currently target a Jetson Nano SD card image flashed with JetPack 4.4. These containers will not work with other version of JetPack.

???+ info
    If you are using a 3rd party JetBot kit, depending on the kit, it may require a customized software setup specific to the kit.

    Please check the manufacture's set up instruction.

## Step 1. Setup Jetson Nano

If you haven't already, go through the initial setup of Jetson Nano.<br>
You can use your existing Jetson Nano set up (microSD card), as long as you have enough storage space left.

???+ hint
    For this, we'll assume you've set up your Jetson Nano using the **online Getting Started guide**.
        
     - [Getting Started With Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

???+ info
    For getting the Wi-Fi connection to Jetson from your computer, check the [Wi-fi setup](wifi_setup.md) documentation.

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

???+ info
    If you are testing a repo/branch that has containers images hosted on NGC, you need to log into the NGC rfegistry first.
    
    Log into NGC, and go to the [Setup > API Key](https://ngc.nvidia.com/setup/api-key) section.
    If you have not generated your API Key, click on the button "**Generate API Key**" at the right upper corner of the page, and save the API key for the future use.
    
    Then, enter the following command on your Jetson and follow the prompts.

    ```bash
    $ sudo docker login nvcr.io
    
    Username: $oauthtoken
    Password: <You Key>
    ```

    For the username, enter `$oauthtoken` exactly as shown. It is a special authentication token for all users.


Now you can go to ``https://<jetbot_ip>:8888`` from a web browser and start programming JetBot!

You can do this from any machine on your local network.  The password to log in is ``jetbot``.

![](https://user-images.githubusercontent.com/25759564/92091965-51ae4f00-ed86-11ea-93d5-09d291ccfa95.png)


???+ caution
    If you do work outside the /workspace directory, it will be lost when the container shuts down.

???+ note
    Once you execute the `enable.sh` script, the containers are set to restart automatically when the system boots (with `docker run --restart always` option).

    So the next time you turn-on your JetBot, even without logging in, you will see the IP address of your JetBot conveniently displayed on the small OLED display (if it is configured to connect to the Wi-Fi network).

???+ note
    Calling `enable.sh` will cause the containers to automatically start at boot. To disable this behavior, call

    ```bash
    cd ~/jetbot/docker
    ./disable.sh
    ```

    This stops and removes the runnig JetBot containers.<br>
    JetBot containers will not come back on when you restart the system.

