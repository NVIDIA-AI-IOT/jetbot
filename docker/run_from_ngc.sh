#!/usr/bin/env bash

# find container tag from L4T version
source tag.sh

JUPYTER_WORKSPACE=${1:-$HOME}  # default to $HOME

sudo docker run -it -d \
	--runtime nvidia \
       	--network host \
	--privileged \
	--device /dev/video* \
	--volume /dev/bus/usb:/dev/bus/usb \
	--volume /tmp/argus_socket:/tmp/argus_socket \
	-p 8888:8888 \
	-v ${JUPYTER_WORKSPACE}:/workspace \
	--workdir /workspace \
	--name=jetbot_uni \
	--memory=1000m \
	--memory-swap=3G \
	$CONTAINER_IMAGE
