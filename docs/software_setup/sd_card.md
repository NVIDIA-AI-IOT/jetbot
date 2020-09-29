???+ caution
    If you are using a 3rd party JetBot kit, depending on the kit, it may require a customized software setup specific to the kit.  
    Please check the manufacture's set up instruction.


This page details the software setup required to run JetBot.

### Step 1 - Flash JetBot image onto SD card

1. Download the expandable JetBot SD card image [jetbot_image_v0p4p0.zip](https://drive.google.com/open?id=1G5nw0o3Q6E08xZM99ZfzQAe7-qAXxzHN)

    ???+ info
        The above image is based on JetPack 4.3.  The previous image based on JetPack 4.2 may be found here: [jetbot_image_v0p3p2.zip](https://drive.google.com/open?id=1GF2D814hkViwluZ5SgNKW56cQu_5Ekt5).

2. Insert an SD card into your desktop machine
3. Using [Etcher](https://www.balena.io/etcher/), select the ``jetbot_image_v0p4p0.zip`` image and flash it onto the SD card
4. Remove the SD card from your desktop machine

### Step 2 - Boot Jetson Nano

1. Insert the SD card into your Jetson Nano (the micro SD card slot is located 
   under the module)

2. Connect the monitor, keyboard, and mouse to the Nano
3. Power on the Jetson Nano by connecting the micro USB charger to the micro USB port

    ???+ danger
        Important! We recommend first booting the Jetson Nano once without the piOLED / motor driver connected.
        This way you can check to make sure the system boots properly from the SD card image without worrying about hardware issues.  After you've verified that it boots, reconnect the piOLED, double check your wiring, and boot again.

### Step 3 - Connect JetBot to WiFi

1. Log in using the user ``jetbot`` and password ``jetbot``

2. Connect to a WiFi network using the Ubuntu desktop GUI

Your Jetson Nano should now automatically connect to the WiFi at boot and display it's IP address on the piOLED display.

### Step 4 - Connect to JetBot from web browser

After your robot is connected to WiFi, you can connect to the robot from a web browser by performing the following steps

1. Shutdown JetBot using the Ubuntu GUI

2. Unplug your HDMI monitor, USB keyboard, mouse and power supply from Jetson Nano
3. Power the JetBot from the USB battery pack by plugging in the micro-USB cable
4. Wait a bit for JetBot to boot
2. Check the IP address of your robot on the *piOLED* display screen.  Enter this in place of ``<jetbot_ip_address>`` in the next command
3. Navigate to ``http://<jetbot_ip_address>:8888`` from your desktop's web browser

???+ info
    You shouldn't need to connect your robot to a monitor past this step! 

### Step 5 - Install latest software (optional)

The JetBot GitHub repository may contain software that is newer than that pre-installed
on the SD card image.  To install the latest software:

1. If you haven't already, connect to your robot by going to ``http://<jetbot_ip_address>:8888``

2. Click the ``+`` icon to open the Jupyter Lab launcher
3. Launch a new terminal
2. Get and install the latest JetBot repository from GitHub by entering the following commands
    ```bash
    git clone https://github.com/NVIDIA-AI-IOT/jetbot
    cd jetbot
    sudo python3 setup.py install
    ``` 
3. Replace the old notebooks with the new notebooks by entering
    ```bash
    sudo apt-get install rsync
    rsync jetbot/notebooks ~/Notebooks
    ```

### Step 6 - Configure power mode

To ensure that the Jetson Nano doesn't draw more current than the battery pack can supply,
place the Jetson Nano in ``5W`` mode by calling the following command

1. If you haven't already, connect to your robot by going to ``http://<jetbot_ip_address>:8888``

2. Click the ``+`` icon to open the Jupyter Lab launcher
3. Launch a new terminal
4. Select 5W power mode

    ```bash
    sudo nvpmodel -m1
    ```
5. Verify the Jetson Nano is in 5W power mode
    ```bash
    sudo nvpmodel -q
    ```
