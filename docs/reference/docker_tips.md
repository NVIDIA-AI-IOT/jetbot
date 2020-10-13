# Docker Tips

## Using Nvidia GPU Cloud (NGC)

The standard JetBot containers are hosted on docker hub, but for development or testing purposes, you may wish to use Nvidia GPU Cloud. To access containers on NGC, you need to sign into the NGC registry. To do this:

1. Log into ngc.nvidia.com

2. Generated your API Key

    1. Navigate to Setup > API Key
    2. Click on "Generate API Key" at the right upper corner of the page
    3. Copy the API key for future use

3. On your Jetson, sign into the NGC registry using the generated key

    ```bash
    $ sudo docker login nvcr.io
    
    Username: $oauthtoken
    Password: <Your Generated Key>
    ````

For the username, enter `$oauthtoken` exactly as shown. It is a special authentication token for all users.


## Using custome Jupyter Lab workspace directory

If you do work outside the /workspace directory, it will be lost when the container shuts down.

## Disabling containers

Once you execute the `enable.sh` script, the containers are set to restart automatically.
This means you can shut down your Jetson, and when you reboot the containers will run and you don't need to repeat this process. 

To prevent the containers from starting automatically, just call the disable.sh script.

    ```bash
    cd ~/jetbot/docker
    ./disable.sh
    ```

