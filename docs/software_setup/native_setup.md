# Native JetBot Setup (without Docker)

This page details how you can configure your Jetson system to use JetBot without Docker.  This is handy when you want to prototype without worrying about docker semantics, or have other reasons to work outside of a docker environment

> If you see any issues with these instructions or have any questions, please feel free to open an issue on github [here](https://github.com/NVIDIA-AI-IOT/jetbot/issues).

## Instructions

### Step 1 - Install dependencies
1. Install NVIDIA JetPack, including NVIDIA TensorRT following [these instructions](https://developer.nvidia.com/embedded/jetpack).
2. Install PyTorch following [this guide](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-11-now-available/72048) provided on the NVIDIA devtalk forums.
3. Install Node JS to support Jupyter Lab

    ```bash
    curl -sL https://deb.nodesource.com/setup_10.x | bash -
    sudo apt-get install -y nodejs libffi-dev
    ```

4. Install Jupyter Lab to support web-programming JetBot

    ```bash
    sudo python3 -m pip install jupyter jupyterlab
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    ```

5. Install Jupyter Clickable Image widget (to support road following example).
    
    ```bash
    sudo apt-get install -y libssl1.0-dev && \
    git clone https://github.com/jaybdub/jupyter_clickable_image_widget && \
    cd jupyter_clickable_image_widget && \
    git checkout tags/v0.1 && \
    sudo pip3 install -e . && \
    jupyter labextension install js && \
    jupyter lab build
    cd ..
    ```

6. Install other miscellaneous dependencies

    ```bash
    sudo apt-get update && apt-get install -y supervisor unzip
    sudo apt install -y python3-smbus && pip3 install pyzmq
    ```

7. (optional) Install torch2trt to support TensorRT accelerated AI models

    ```bash
    git clone https://github.com/NVIDIA-AI-IOT/torch2trt
    cd torch2trt
    python3 setup.py install
    cd ..
    ```

8. Install the JetBot Python package
    
    ```bash
    git clone https://github.com/NVIDIA-AI-IOT/jetbot
    cd jetbot
    sudo python3 setup.py install
    # if you plan to modify the jetbot python package, call this instead: sudo python3 setup.py develop

    ```


### Step 2 - Set the Jupyter lab password

Call the following from a terminal
```bash
jupyter notebook password
# enter password
```

You could now test the JetBot notebooks by running

```bash
cd jetbot
jupyter lab --ip=0.0.0.0 --no-browser --allow-root
```

and then navigating to ``https://<jetbot_ip>:8888`` and signing in with the password you set.

However, it is convenient to have this server start automatically, which we will detail next.

### Step 3 - Create a system service to start the Jupyter Lab server at boot

1. Create file named ``jetbot_jupyter.service`` and add the following content.  

    ```bash
    [Unit]
    Description=Jupyter Notebook 

    [Service]
    Type=simple
    User=jetson
    ExecStart=/bin/sh -c "jupyter lab --ip=0.0.0.0 --no-browser --allow-root"
    WorkingDirectory=/home/jetson
    Restart=Always

    [Install]
    WantedBy=multi-user.target
    ```

    > Note: If you have a username other than "jetson" or want to launch Jupyter from a directory other than "/home/jetson", modify the file "User" and "WorkingDirectory" fields accordingly.

2. Copy the file to the directory ``/etc/systemd/system`` so it can be discovered as a system service.

    ```bash
    sudo cp jetbot_jupyter.service /etc/systemd/system/jetbot_jupyter.service
    ```

3. Enable the system service to run at boot

    ```bash
    sudo systemctl enable jetbot_jupyter
    ```

Now, when you re-boot your Jetson, the Jupyter lab server should start in the background.  

That's great, but in order to connect to the server, you need to know it's IP address.  The last step will be to enable a system service that displays the IP address on the JetBot's PiOLED display upon boot.


### Step 4 - Create system service to show the IP address upon boot

This is very similar to creating a service for the Jupyter Lab server, we're just changing the application that's launched

1. Create a file named ``jetbot_display.service`` and add the following content.

    ```bash
    [Unit]
    Description=Jupyter Notebook 

    [Service]
    Type=simple
    User=jetson
    ExecStart=/bin/sh -c "python3 -m jetbot.apps.stats"
    WorkingDirectory=/home/jetson
    Restart=Always

    [Install]
    WantedBy=multi-user.target
    ```

2. Copy the file to the directory ``/etc/systemd/system`` so it can be discovered as a system service.

    ```bash
    sudo cp jetbot_display.service /etc/systemd/system/jetbot_display.service
    ```

3. Enable the system service to run at boot

    ```bash
    sudo systemctl enable jetbot_display
    ```

That's it!  Now you should be able to reboot the JetBot, and it's IP address should automatically show up on the PiOLED display.

We hope this helps you create a custom native system configuration for using JetBot.  If you have any questions or see any issues with this guide, please [create an issue on GitHub](https://github.com/NVIDIA-AI-IOT/jetbot/issues).

Happy hacking!