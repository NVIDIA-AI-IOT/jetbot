# JetBot Docker

This directory contains scripts to build the JetBot docker containers.  

## Quick Start

### Step 1 - Build All Containers

```bash
cd docker
./build.sh
```

### Step 2 - Launch all containers

```bash
./run.sh $HOME   # we'll use home directory as working directory, set this as you please.
```

Now you can go to ``https://<jetbot_ip>:8888`` and start programming JetBot from your web browser.
The directory you specify to ``./run.sh`` will be mounted as a volume in the jupyter container 
at the location ``/workspace``.  This means the work you in the ``/workspace`` folder inside container
is saved.  Please note, if you work outside of that directory it will be lost when the container shuts down.

## Containers

We have developed several containers related to JetBot.

Please note, to build the containers individually, set the ``JETBOT_VERSION``
environment variable.  This will apply a tag to each container.  For example

```
export JETBOT_VERSION=jp44-master  # tag for jetpack 44 \ jetbot master
```

### Container 1 - jetbot-base

This container includes

* PyTorch
* TensorFlow
* Jupyter Lab
* JetBot Python API

Among other small related dependencies.

#### Build

```bash
cd docker/base
./build.sh
```

Other containers depend on this, it's typically not run directly.  You could 
build your own container on top of this.

### Container 2 - jetbot-display

This container includes

* A launch script to show JetBot stats on PiOLED display

#### Build

```bash
cd docker/display
./build.sh
```

#### Run

```bash
cd docker/display
./run.sh
```

### Container 3 - jetbot-camera

This container includes

* A launch script to publish camera images using ZMQ for access in other containers

#### Build

```bash
cd docker/camera
./build.sh
```

#### Run

```bash
cd docker/camera
./run.sh
```

### Container 4 - jetbot-jupyter

This container includes

* A launch script to run jupyter lab at the specified working directory

#### Build

```bash
cd docker/jupyter
./build.sh
```

#### Run

```bash
cd docker/jupyter
./run.sh $HOME
```