# Docker

Since the release of JetPack 4.4, NVIDIA Jetson has supported [Cloud-Native](https://developer.nvidia.com/embedded/jetson-cloud-native) development. This makes it easy to develop Docker containers which package software along with it's dependencies.  This containerization ensures that no-matter your system setup, it's easy to install and run software in a reproducible way.  

We've included containers which package JetBot and it's various dependencies.  Compared to our previous method of releasing JetBot as a large SD card image, this makes it much easier to install JetBot
on your existing Jetson system.  Rather than downloading an entirely new SD card image, you just run a command to launch the docker containers and turn your Jetson Nano into a JetBot.

## Quick Start

### Step 1 - Build All Containers

```bash
cd docker
./build.sh
```

### Step 2 - Enable all containers

```bash
sudo systemctl enable docker   # enable docker daemon at boot
./enable.sh $HOME   # we'll use home directory as working directory, set this as you please.
```

Now you can go to ``https://<jetbot_ip>:8888`` and start programming JetBot from your web browser.
The directory you specify to ``./run.sh`` will be mounted as a volume in the jupyter container 
at the location ``/workspace``.  This means the work you in the ``/workspace`` folder inside container
is saved.  Please note, if you work outside of that directory it will be lost when the container shuts down.
