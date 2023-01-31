ARG BASE_IMAGE=dustynv/ros:foxy-pytorch-l4t-r32.7.1
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY ./ ./

RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh

# ENTRYPOINT ["./entrypoint.sh"]