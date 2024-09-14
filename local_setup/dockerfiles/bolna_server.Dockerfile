FROM python:3.10.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    git \
    ffmpeg
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install git+https://github.com/nexa-ai/nexa@master
COPY quickstart_server.py /app/

EXPOSE 5001

CMD ["uvicorn", "quickstart_server:app", "--host", "0.0.0.0", "--port", "5001"]
