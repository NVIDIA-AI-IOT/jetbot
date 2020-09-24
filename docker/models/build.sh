sudo docker build \
    --build-arg BASE_IMAGE=$JETBOT_DOCKER_REMOTE/jetbot:base-$JETBOT_VERSION-$L4T_VERSION \
    -t $JETBOT_DOCKER_REMOTE/jetbot:models-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile .
