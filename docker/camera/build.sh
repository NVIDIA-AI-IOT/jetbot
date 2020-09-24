sudo docker build \
    --build-arg BASE_IMAGE=$JETBOT_DOCKER_REMOTE/jetbot:base-$JETBOT_VERSION-$L4T_VERSION \
    -t $JETBOT_DOCKER_REMOTE/jetbot:camera-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile .
