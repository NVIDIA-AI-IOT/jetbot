#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
${DIR}/create-sdcard-image-from-scratch.sh 2>&1 | tee ~/jetbot-create-sdcard-image.log
