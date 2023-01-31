ARG BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY ./ ./

RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh

# ENTRYPOINT ["./entrypoint.sh"]