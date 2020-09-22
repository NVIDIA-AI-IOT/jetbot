sudo docker build \
    --build-arg BASE_IMAGE=jetbot:base-$JETBOT_VERSION-$L4T_VERSION \
    -t jetbot:display-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile .

