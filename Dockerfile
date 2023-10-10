ARG BUILD_FROM
FROM $BUILD_FROM

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    && curl --silent --show-error --retry 5 \
    "https://bootstrap.pypa.io/get-pip.py" \
    | python3 \
    && pip3 install --no-cache-dir \
    tensorflow==2.5.0 \
    numpy==1.26.0 \
    requests==2.31.0 \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
# Copy data for add-on
COPY rootfs /