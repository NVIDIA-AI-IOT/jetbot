#!/bin/bash

WORKDIR="${HOME}/jetbot_workspace"

if ! [[ -d ${WORKDIR} ]]; then
    mkdir ${WORKDIR} 
fi
sudo cp -r ./notebooks ${WORKDIR}/Notebooks
