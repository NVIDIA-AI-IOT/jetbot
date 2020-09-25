#!/bin/bash

export JETBOT_VERSION=0.4.1

L4T_VERSION_STRING=$(head -n 1 /etc/nv_tegra_release)
L4T_RELEASE=$(echo $L4T_VERSION_STRING | cut -f 2 -d ' ' | grep -Po '(?<=R)[^;]+')
L4T_REVISION=$(echo $L4T_VERSION_STRING | cut -f 2 -d ',' | grep -Po '(?<=REVISION: )[^;]+')

export L4T_VERSION="$L4T_RELEASE.$L4T_REVISION"

if [[ "$L4T_VERSION" == "32.4.3" ]]
then
    # docker hub
    export JETBOT_DOCKER_REMOTE=jetbot
elif [[ "$L4T_VERSION" == "32.4.4" ]]
then
    export JETBOT_DOCKER_REMOTE=nvcr.io/ea-linux4tegra
fi


