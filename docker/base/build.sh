cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ../.. # copy to jetbot root

BASE_IMAGE=$1

if [ -z $BASE_IMAGE ]; then
	if [[ "$L4T_VERSION" == "32.4.3" ]]; then
		BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.4.3-pth1.6-py3
	elif [[ "$L4T_VERSION" == "32.4.4" ]]; then
    		BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.4.4-pth1.6-py3
	fi
fi

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

