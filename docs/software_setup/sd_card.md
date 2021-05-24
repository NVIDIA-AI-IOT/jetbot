# Software Setup (SD Card Image)

This page details how to set up JetBot using the pre-built JetBot SD card image. You may prefer this option if you are new to Jetson Nano, and do not have an existing SD card configured.


## Step 1 - Download the pre-built JetBot SD card image

Download the pre-built JetBot SD card image from the table below.  Make sure to select the version that matches the Jetson you're using  (for example Jetson Nano 2GB).

### Latest Release

| Platform | JetPack Version | JetBot Version | Download | MD5 Checksum | 
|--------|-----------------|----------------|--------|----|
| Jetson Nano 2GB | 4.5 | 0.4.3 | [jetbot-043_nano-2gb-jp45.zip](https://drive.google.com/file/d/1tsuSY3iZrfiKu4ww-RX-eCPcwuT2DPwJ/view?usp=sharing) | e6dda4d13b1b1b31f648402b9b742152 |
| Jetson Nano (4GB) | 4.5 | 0.4.3 | [jetbot-043_nano-4gb-jp45.zip](https://drive.google.com/file/d/1o08RPDRZuDloP_o76tCoSngvq1CVuCDh/view?usp=sharing) | 760b1885646bfad8590633acca014289 |

???+ attention
    To use one of the JetBot sdcard images based on JetPack 4.5, you first need to boot your Jetson Nano using a plain JetPack 4.5 SD card image and run through the operating system setup.
    This will perform a one-time configuration which enables you to use SD card images based on JetPack 4.5 on your device.  You can find the original JetPack SD card images
    here: [JetPack SD card image for Jetson Nano 2GB](https://developer.nvidia.com/jetson-nano-2gb-sd-card-image) and [JetPack SD card image for Jetson Nano (4GB)](https://developer.nvidia.com/jetson-nano-sd-card-image).  After doing this procedure once, you can then use the JetPack 4.5 based JetBot SD card images listed above on your device.


### Old releases

| Platform | JetPack Version | JetBot Version | Download |
|--------|-----------------|----------------|--------|
| Jetson Nano 2GB | 4.4.1 | 0.4.2 | [jetbot-042_nano-2gb-jp441.zip](https://drive.google.com/file/d/1uiWz6QTcqB3wzN81gdv_zY8t_V3ZzkNE/view) |
| Jetson Nano (4GB) | 4.4.1 | 0.4.2 | [jetbot-042_nano-4gb-jp441.zip](https://drive.google.com/file/d/1MAX1ibJvcLulKQeMtxbjMhsrOevBfUJd/view) |
| Jetson Nano 2GB | 4.4.1 | 0.4.1 | [jetbot-041_nano-2gb-jp441.zip](https://drive.google.com/file/d/1d03TOrQyffxFsv_Nhp-XQ7Q3-nCHbT9a/view) |
| Jetson Nano (4GB) | 4.4.1 | 0.4.1 | [jetbot-041_nano-4gb-jp441.zip](https://drive.google.com/file/d/1yQ5MEiiBxbytCXHFPPBi-5SAxWklhZQA/view) |
| Jetson Nano (4GB) | 4.3 | 0.4.0 | [jetbot_image_v0p4p0.zip](https://drive.google.com/open?id=1G5nw0o3Q6E08xZM99ZfzQAe7-qAXxzHN) |
| Jetson Nano (4GB) | 4.2 | 0.3.2 | [jetbot_image_v0p3p2.zip](https://drive.google.com/open?id=1GF2D814hkViwluZ5SgNKW56cQu_5Ekt5) | 

## Step 2 - Flash JetBot image onto SD card

1. Insert an SD card into your desktop machine

3. Using [Etcher](https://www.balena.io/etcher/), select the image you downloaded above and flash it onto the SD card.

4. Remove the SD card from your desktop machine

## Step 3 - Boot Jetson Nano

1. Insert the SD card into your Jetson Nano (the micro SD card slot is located 
   under the module)

2. Connect the monitor, keyboard, and mouse to the Nano
3. Power on the Jetson Nano by connecting the micro USB (for Jetson Nano (4GB)) or USB-C (for Jetson Nano 2GB) charger to the port

    ???+ attention 
        We recommend first booting the Jetson Nano once without the piOLED / motor driver connected.

        This way you can check to make sure the system boots properly from the SD card image without worrying about hardware issues.  After you've verified that it boots, reconnect the piOLED, double check your wiring, and boot again.

## Step 4 - Connect JetBot to WiFi

Next you'll need to connect to WiFi.  To reduce memory consumption, we disable the Ubuntu GUI in the latest JetBot SD card image.  For this reason, you'll need to use the command line to connect to WiFi.

1. Log in using the user ``jetbot`` and password ``jetbot``
    
2. Connect to a WiFi network using the following command

    ```bash
    sudo nmcli device wifi connect <SSID> password <PASSWORD>
    ```
    
Your Jetson Nano should now automatically connect to the WiFi at boot and display it's IP address on the piOLED display.

???+ tip
    If you're having trouble figuring out how to get connected to Wi-Fi, check out the [Wi-Fi setup](wifi_setup.md) page for more detailed instructions 

## Step 5 - Connect to JetBot from web browser

After your robot is connected to WiFi, you no longer need to have the robot connected by a monitor.  You can connect to the robot from your laptop's web browser by performing the following steps

1. Shutdown JetBot using the command line

    ```bash
    sudo shutdown now
    ```

2. Unplug your HDMI monitor, USB keyboard, mouse and power supply from Jetson Nano

3. Power the JetBot from the USB battery pack by plugging in the micro-USB cable
4. Wait a bit for JetBot to boot
2. Check the IP address of your robot on the *piOLED* display screen.  Enter this in place of ``<jetbot_ip_address>`` in the next command
3. Navigate to ``http://<jetbot_ip_address>:8888`` from your desktop's web browser. You can do this from any machine on your local network.  
4. Sign in using the password ``jetbot``.

That's it, you've now accessed JetBot's remote programming environment! 

You will be presented with a view similar to the following. 

![](../images/docker_jupyter-on-browser.png)

Here you can easily access the JetBot examples!  From this point on, when you power on the JetBot, it should automatically connect to WiFi and display it's IP address.  So all you need to do is reconnect using your web browser to start programming!

Now that you're finished setting up your JetBot, you're ready to run the [examples](../examples/basic_motion.md).
