# How to set up jetbot using Docker

This document explains how to set up [`jetbot`](https://github.com/NVIDIA-AI-IOT/jetbot) in a container on Jetson.

This is to provide an alternative path to using the original JetBot dedicated SD card image.<br>
With this container-based setup, you can quickly start using JetBot on a regular SD card image.

## How to start JetBot container

On your Jetson machine (container's host);

```bash
git clone https://github.com/NVIDIA-AI-IOT/jetbot
cd jetbot/
./script/configure_jetson.sh
cd docker/
./set_nvidia_runtime.sh
./build.sh
./enable.sh
```

You should see your JetBot container running and it should look like

```bash
$ sudo docker ps 

```
## How to start using JetBot in container

Once you start the container, you should see the OLED display on your JetBot showing the IP address.

You can use your separate client machine (ex. laptop) to open the Jupyter Lab on its web browser.
> Jupyter Lab password is still `jetbot`.

<a href="https://user-images.githubusercontent.com/25759564/91165191-1eccd280-e685-11ea-809f-9aa2dbcc718c.png"><img src="https://user-images.githubusercontent.com/25759564/91165191-1eccd280-e685-11ea-809f-9aa2dbcc718c.png" height="480"></a>

## Known limitations

- To use a notebook that uses the CSI camera for the 2nd time, you need to restart the JetBot container from your container host environment.

## Tips

JetBot's services (`jetbot_display.service` and `jetbot_jupyter`) are runnign as a subprocess of `supervisord`.
You can check what subprocesses (JetBot services) are running using `supervisorctl`.

```bash
root@nano-4-4:/jetbot_dir# supervisorctl status
jetbot_display                   RUNNING   pid 16, uptime 0:02:42
jetbot_jupyter                   RUNNING   pid 15, uptime 0:02:42
```

You can choose to stop/restart a subprocess.

```bash
root@nano-4-4:/jetbot_dir# supervisorctl stop jetbot_jupyter
jetbot_jupyter: stopped
root@nano-4-4:/jetbot_dir# supervisorctl status
jetbot_display                   RUNNING   pid 16, uptime 0:03:30
jetbot_jupyter                   STOPPED   Aug 25 10:36 AM
```

## Test

It is tested on the following platform and the JetPack image.

- Jetson Nano Developer Kit - [JetPack 4.4](https://developer.nvidia.com/embedded/downloads#?search=Jetson%20Nano%20Developer%20Kit%20SD%20Card%20Image)

