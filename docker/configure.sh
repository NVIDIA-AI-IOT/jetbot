#!/bin/bash

export JETBOT_VERSION=0.4.3

L4T_VERSION_STRING=$(head -n 1 /etc/nv_tegra_release)
L4T_RELEASE=$(echo $L4T_VERSION_STRING | cut -f 2 -d ' ' | grep -Po '(?<=R)[^;]+')
L4T_REVISION=$(echo $L4T_VERSION_STRING | cut -f 2 -d ',' | grep -Po '(?<=REVISION: )[^;]+')


export L4T_VERSION="$L4T_RELEASE.$L4T_REVISION"

if [[ $L4T_VERSION = "32.4.3" ]]
then
	export JETBOT_BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.4.3-pth1.6-py3
elif [[ "$L4T_VERSION" == "32.4.4" ]]
then
	export JETBOT_BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.4.4-pth1.6-py3
elif [[ "$L4T_VERSION" == "32.5.0" ]]
then
    export JETBOT_BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.6-py3
	# export JETBOT_BASE_IMAGE=nvcr.io/ea-linux4tegra/l4t-pytorch:r32.5.0-pth1.7-py3	# from bash history of pre-built 2GB image: jetbot-043_nano-2gb-jp45.zip
else
	echo "JETBOT_BASE_IMAGE not found for ${L4T_VERSION}.  Please manually set the JETBOT_BASE_IMAGE environment variable. (ie: export JETBOT_BASE_IMAGE=...)"
fi

export JETBOT_DOCKER_REMOTE=jetbot

./set_nvidia_runtime.sh
sudo systemctl enable docker

# check system memory
SYSTEM_RAM_KILOBYTES=$(awk '/^MemTotal:/{print $2}' /proc/meminfo)

if [ $SYSTEM_RAM_KILOBYTES -lt 3000000 ]
then
    export JETBOT_JUPYTER_MEMORY=500m
    export JETBOT_JUPYTER_MEMORY_SWAP=3G
fi

