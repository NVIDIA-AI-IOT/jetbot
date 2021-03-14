WORKSPACE=$1
JETBOT_CAMERA=${2:-opencv_gst_camera}

# set default swap limit as unlimited
if [[ -z "$JETBOT_JUPYTER_MEMORY_SWAP" ]]
then
	export JETBOT_JUPYTER_MEMORY_SWAP=-1
fi

if [[ -z "$JETBOT_JUPYTER_MEMORY" ]]
then

	sudo docker run -it -d \
	    --restart always \
	    --runtime nvidia \
	    --network host \
	    --privileged \
	    --device /dev/video* \
	    --volume /dev/bus/usb:/dev/bus/usb \
	    --volume /tmp/argus_socket:/tmp/argus_socket \
	    -p 8888:8888 \
	    -v $WORKSPACE:/workspace \
	    --workdir /workspace \
	    --name=jetbot_jupyter \
	    --memory-swap=$JETBOT_JUPYTER_MEMORY_SWAP \
	    --env JETBOT_DEFAULT_CAMERA=$JETBOT_CAMERA \
	    $JETBOT_DOCKER_REMOTE/jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION

else

	sudo docker run -it -d \
	    --restart always \
	    --runtime nvidia \
	    --network host \
	    --privileged \
	    --device /dev/video* \
	    --volume /dev/bus/usb:/dev/bus/usb \
	    --volume /tmp/argus_socket:/tmp/argus_socket \
	    -p 8888:8888 \
	    -v $WORKSPACE:/workspace \
	    --workdir /workspace \
	    --name=jetbot_jupyter \
	    --memory=$JETBOT_JUPYTER_MEMORY \
	    --memory-swap=$JETBOT_JUPYTER_MEMORY_SWAP \
	    --env JETBOT_DEFAULT_CAMERA=$JETBOT_CAMERA \
	    $JETBOT_DOCKER_REMOTE/jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION

fi
