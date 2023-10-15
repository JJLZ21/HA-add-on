# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    \
    && pip3 install --no-cache-dir \
    requests==2.31.0 \
    \
    && rm -rf /var/lib/apt/lists/*

# Copy root filesystem
COPY rootfs /
