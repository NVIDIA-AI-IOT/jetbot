cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ../.. # copy to jetbot root

if [[ "$L4T_VERSION" == "32.4.3" ]]
then
    BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.4.3-pth1.6-py3
elif [[ "$L4T_VERSION" == "32.4.4" ]]
then
    BASE_IMAGE=nvcr.io/ea-linux4tegra/l4t-pytorch:r32.4.4-pth1.6-py3
fi

sudo docker build \
    --build-arg BASE_IMAGE=$BASE_IMAGE \
    -t jetbot/jetbot:base-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile \
    ../..  # jetbot repo root as context

