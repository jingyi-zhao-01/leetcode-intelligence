FROM node:22-bookworm-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends openssl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY package.json package-lock.json ./
COPY services/leetcode-intelligence-service/package.json services/leetcode-intelligence-service/package.json

COPY services/shared/prisma/schema.prisma services/shared/prisma/schema.prisma
RUN npm ci

COPY services/leetcode-intelligence-service services/leetcode-intelligence-service

RUN npm exec prisma -- generate --generator jsclient --schema services/shared/prisma/schema.prisma

ENV INTELLIGENCE_HOST=0.0.0.0 \
    INTELLIGENCE_PORT=8030

EXPOSE 8030

CMD ["npm", "run", "--workspace", "services/leetcode-intelligence-service", "intelligence-server"]
