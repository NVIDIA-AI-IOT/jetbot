# Running JetBot in Docker Container

This directory contains scripts to build and run the JetBot docker containers.  

## Quick Start 

Docker container images for this project are hosted on NGC.

### Step 1 - Configure Docker host (Jetson)

```bash
cd jetbot/
./script/configure_jetson.sh
cd docker/
./set_nvidia_runtime.sh
```

### Step 2 - Pull from NGC and launch the container

```bash
./run_from_ngc.sh
```
### Step 3 - Open JupyterLab on a web browser

Once you start the container, you should see the OLED display on your JetBot showing the IP address.

You can use your separate client machine (ex. laptop) to open the Jupyter Lab on its web browser.
> Jupyter Lab password is still `jetbot`.

<a href="https://user-images.githubusercontent.com/25759564/92091965-51ae4f00-ed86-11ea-93d5-09d291ccfa95.png"><img src="https://user-images.githubusercontent.com/25759564/92091965-51ae4f00-ed86-11ea-93d5-09d291ccfa95.png" height="480"></a>

### Stopping 

```bash
sudo docker stop jetbot_uni
```


## Building the Container

If you wish to re-build the container or build your own, you can use the [`docker/build.sh`](build.sh) script which builds the project's [`Dockerfile`](./Dockerfile):

### Build

```bash
cd jetbot/
./script/configure_jetson.sh
cd docker/
./set_nvidia_runtime.sh
./build.sh
```

### Enable to always launch on system boot

```bash
./enable.sh
```

### Stop the container

```bash
./disable.sh
```
