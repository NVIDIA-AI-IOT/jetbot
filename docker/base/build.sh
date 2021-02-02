cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ../.. # copy to jetbot root

sudo docker build \
    --build-arg BASE_IMAGE=$JETBOT_BASE_IMAGE \
    -t $JETBOT_DOCKER_REMOTE/jetbot:base-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile \
    ../..  # jetbot repo root as context

