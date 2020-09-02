#!/bin/bash

WORKDIR="${HOME}/jetbot_workspace"

if ! [[ -d ${WORKDIR} ]]; then
    mkdir ${WORKDIR} 
fi
cp -r ./notebooks ${WORKDIR}/Notebooks
