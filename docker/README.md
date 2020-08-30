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

## Use Individual Containers

It's possible to run the JetBot containers individually as well.  You may want to do this if for example, you are using a different Camera with JetBot, and don't need to run our CSI camera publisher container.  We currently have three executable containers.

### Jupyter Container

This container Launches the Jupyter Lab programming environment at a specified working directory.  

#### Build 

Build this container with the following command

```bash
cd docker/jupyter
./build.sh
```

#### Run

And then enable it to run at boot by calling

```bash
cd docker/jupyter
./enable.sh $HOME
```

### Display Container 

This container displays various JetBot system statistics, including it's IP address on the connected PiOLED screen.

#### Build 

Build this container with the following command

```bash
cd docker/display
./build.sh
```

#### Run

And then enable it to run at boot by calling

```bash
cd docker/display
./enable.sh $HOME
```

### Camera Container 

This container publishes Camera images using [ZeroMQ](https://zeromq.org/).  The images may then be received by notebooks using the ``ZmqCamera`` class (or similarily, the ``Camera`` class, since this is the default camera implementation).

#### Build 

Build this container with the following command

```bash
cd docker/camera
./build.sh
```

#### Run

And then enable it to run at boot by calling

```bash
cd docker/camera
./enable.sh $HOME
```

## Make your own Container

If you have configured your JetBot with new software, and want to package a container of your own, we recommend referencing one of the JetBot containers we've developed.  

In JetBot, we package each container in it's own folder.  You can do
this differently if you please, we've just found it a decent
form of organization.  In this folder we commonly include three files

* A [Dockerfile](https://docs.docker.com/engine/reference/builder/) which describes the steps to install software inside our container, and perform any environment setup the container needs
* A ``build.sh``bash script, which is a convenience script for building the container in a typical configuration
* An ``enable.sh`` (or ``run.sh``) bash script, which is another convenience script for
running the container in a typical configuration.  We use the notation ``enable.sh`` for containers that automatically restart at boot (``--restart always``), and ``run.sh`` for containers which run once.

For example, we defined the following three files for our Jupyter Lab container.

=== "Dockerfile"

    ```
    --8<-- "./docker/jupyter/Dockerfile"
    ```

=== "build.sh"

    ```
    --8<-- "./docker/jupyter/build.sh"
    ```
    
=== "enable.sh"

    ```
    --8<-- "./docker/jupyter/enable.sh"
    ```

Notice we use the ``JETBOT_VERSION`` environment variable to specify
the tag for our containers.  To build the Jupyter container, based on other containers tagged ``jp44-master`` for example, you would need to set

```bash
export JETBOT_VERSION=jp44-master
cd jupyter
./build.sh
```