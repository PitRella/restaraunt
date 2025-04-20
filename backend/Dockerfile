FROM python:3.12-slim AS builder
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

FROM builder AS installer
COPY backend/requirements.txt .
COPY backend/ .
RUN pip install --upgrade pip && pip install -r requirements.txt

FROM installer AS application
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1