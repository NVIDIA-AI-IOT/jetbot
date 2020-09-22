sudo docker build \
    --build-arg BASE_IMAGE=jetbot/jetbot:models-$JETBOT_VERSION-$L4T_VERSION \
    -t jetbot/jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile .
