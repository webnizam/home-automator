ARG BASE_IMAGE=nvcr.io/nvidia/dli/dli-nano-ai
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY ./ ./

RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh

# ENTRYPOINT ["./entrypoint.sh"]