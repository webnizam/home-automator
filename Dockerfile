ARG BASE_IMAGE=nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.6.1
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY ./ ./

RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]