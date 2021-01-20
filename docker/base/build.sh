cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ../.. # copy to jetbot root

BASE_IMAGE=$1

echo "sudo docker build \
    --build-arg BASE_IMAGE=$BASE_IMAGE \
    -t jetbot/jetbot:base-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile \
    ../.."  # jetbot repo root as context

sudo docker build \
    --build-arg BASE_IMAGE=$BASE_IMAGE \
    -t jetbot/jetbot:base-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile \
    ../..  # jetbot repo root as context

