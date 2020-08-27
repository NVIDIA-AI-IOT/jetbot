ARG BASE_IMAGE=jetbot-deps:jp44
FROM ${BASE_IMAGE}

ENV JETBOT_REPO_DIR=/opt/jetbot

# ==============
# INSTALL JETBOT
# ==============
COPY . ${JETBOT_REPO_DIR}
RUN cd ${JETBOT_REPO_DIR} && python3 setup.py install