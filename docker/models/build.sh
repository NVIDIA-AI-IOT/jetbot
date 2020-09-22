sudo docker build \
    --build-arg BASE_IMAGE=jetbot:base-$JETBOT_VERSION-$L4T_VERSION \
    -t jetbot:models-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile .
