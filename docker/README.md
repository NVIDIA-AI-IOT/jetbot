# JetBot Docker

This directory contains scripts to build the JetBot docker containers.  

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
