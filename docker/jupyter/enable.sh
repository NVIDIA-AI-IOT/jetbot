WORKSPACE=$1
JETBOT_CAMERA={$2:-opencv_gst_camera}

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
    --env JETBOT_DEFAULT_CAMERA=$JETBOT_CAMERA \
    jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION
