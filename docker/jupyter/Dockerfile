ARG BASE_IMAGE=jetbot-models:jp44
FROM ${BASE_IMAGE}

ARG JUPYTER_PASSWORD=jetbot
ENV JUPYTER_WORKDIR=/workspace
WORKDIR /workspace

RUN apt-get update && \
    apt-get install -y ssh

# ====================
# SET JUPYTER PASSWORD
# ====================
ENV JUPYTER_PASSWORD=${JUPYTER_PASSWORD}
RUN jupyter lab --generate-config -y
RUN python3 -c "from notebook.auth.security import set_password; set_password('${JUPYTER_PASSWORD}', '/root/.jupyter/jupyter_notebook_config.json')"    

ENV SHELL /bin/bash

CMD cd $JUPYTER_WORKDIR && jupyter lab --ip 0.0.0.0 --port 8888 --allow-root
