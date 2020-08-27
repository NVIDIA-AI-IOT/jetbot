CONTAINER=jetbot-deps:jp44
WORKSPACE=$1

sudo docker run -it --rm \
    --runtime nvidia \
    --network host \
    --privileged \
    --device /dev/video* \
    --volume /dev/bus/usb:/dev/bus/usb \
    --volume /tmp/argus_socket:/tmp/argus_socket \
    -p 8888:8888 \
    -v $WORKSPACE:/workspace \
    --workdir /workspace \
    $CONTAINER