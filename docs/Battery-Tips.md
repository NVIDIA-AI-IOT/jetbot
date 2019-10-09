This page has tips related to battery charging and usage for [this battery](https://amzn.to/2WRcIUe).

### Best charging practice

We recommend the following steps for charging your battery

1. Shutdown JetBot (from Jupyter Lab terminal)

    ```bash
    sudo shutdown now
    ```
2. Unplug Jetson Nano and the motor driver the from battery pack
3. Insert the charger into the battery pack
4. Wait for the battery to charge
5. Unplug the charger from the battery pack
6. Plug Jetson Nano and the motor driver back into battery pack

### Prevent high current shutdown

In high power mode, it is possible to draw more current than the battery can supply.  To prevent this:

1. Select 5W power mode 

    ```bash
    sudo nvpmodel -m1
    ```
2. Confirm power mode

    ```bash
    nvpmodel -q
    ```


[![Analytics](https://ga-beacon.appspot.com/UA-135919510-1/jetbot/docs/Battery-Tips/?pixel)](https://github.com/igrigorik/ga-beacon)