FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libatomic1 nodejs npm \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
COPY services ./services
COPY shared ./shared

RUN uv sync --frozen --no-dev \
    && cd services/submission-server && npm install \
    && cd /app/services/mcp-server && npm install

CMD ["uv", "run", "python", "--version"]
