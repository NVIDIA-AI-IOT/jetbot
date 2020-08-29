#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

python3 ${SCRIPT_DIR}/create_container_autostart_service.py --script_dir=${SCRIPT_DIR}
cat jetbot_container_autostart.service

sudo mv jetbot_container_autostart.service /etc/systemd/system/jetbot_container_autostart.service

sudo systemctl enable jetbot_container_autostart
sudo systemctl start jetbot_container_autostart
