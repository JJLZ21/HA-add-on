FROM ghcr.io/hassio-addons/debian-base:6.2.3


RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    \
    && pip3 install --no-cache-dir \
    tensorflow \
    requests==2.31.0 \
    \
    && rm -rf /var/lib/apt/lists/*

CMD ["echo", "done!"]
# COPY rootfs /