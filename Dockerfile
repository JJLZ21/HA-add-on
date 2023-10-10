ARG BUILD_FROM
FROM $BUILD_FROM


RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
    \
    && pip3 install --no-cache-dir \
        onnxruntime==1.15.0 \
        numpy==1.26.0 \
        requests==2.31.0 \
    \
    && rm -rf /var/lib/apt/lists/*


COPY rootfs /