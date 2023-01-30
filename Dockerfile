ARG BASE_IMAGE=nvcr.io/nvidia/l4t-base:r32.4.4
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    libopenblas-dev \
    libopenmpi-dev \
    openmpi-bin \
    openmpi-common \
    gfortran \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN pip3 install --no-cache-dir setuptools Cython wheel
RUN pip3 install --no-cache-dir --verbose numpy
RUN pip3 install --no-cache-dir gdown

WORKDIR /app

RUN gdown https://drive.google.com/uc?id=1e9FDGt2zGS5C5Pms7wzHYRb0HuupngK1

RUN pip3 install torch-1.13.0a0+git7c98e70-cp38-cp38-linux_aarch64.whl

