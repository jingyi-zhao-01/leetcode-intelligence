FROM node:22-bookworm-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends openssl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install workspace dependencies first for better layer caching.
COPY package.json package-lock.json ./
COPY services/leetcode-submission-service/package.json services/leetcode-submission-service/package.json
RUN npm ci

# Copy runtime sources.
COPY services/shared/prisma/schema.prisma services/shared/prisma/schema.prisma
COPY services/leetcode-submission-service services/leetcode-submission-service

# Generate Prisma client from shared schema.
RUN npm exec prisma -- generate --generator jsclient --schema services/shared/prisma/schema.prisma

ENV SUBMISSION_HOST=0.0.0.0 \
    SUBMISSION_PORT=3000

EXPOSE 3000

CMD ["npm", "run", "--workspace", "services/leetcode-submission-service", "submission-server"]
