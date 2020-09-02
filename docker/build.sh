export JETBOT_VERSION=jp44

cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ../ # copy to jetbot repo root

sudo docker build \
	-t jetbot_uni:${JETBOT_VERSION} \
	-f Dockerfile \
	.. # jetbot repo root as context

