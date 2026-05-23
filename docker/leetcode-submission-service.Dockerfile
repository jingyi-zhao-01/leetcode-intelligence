FROM node:22-bookworm-slim AS build

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends openssl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY package.json package-lock.json ./
COPY services/leetcode-submission-service/package.json services/leetcode-submission-service/package.json
RUN npm ci

COPY services/shared/prisma/schema.prisma services/shared/prisma/schema.prisma
COPY services/leetcode-submission-service/tsconfig.json services/leetcode-submission-service/tsconfig.json
COPY services/leetcode-submission-service/src services/leetcode-submission-service/src

RUN npm exec prisma -- generate --generator jsclient --schema services/shared/prisma/schema.prisma
RUN npm run --workspace services/leetcode-submission-service build

FROM node:22-bookworm-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends openssl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY package.json package-lock.json ./
COPY services/leetcode-submission-service/package.json services/leetcode-submission-service/package.json
RUN npm ci --omit=dev

COPY services/shared/prisma/schema.prisma services/shared/prisma/schema.prisma
COPY --from=build /app/services/leetcode-submission-service/dist services/leetcode-submission-service/dist
COPY --from=build /app/node_modules/.prisma node_modules/.prisma
COPY --from=build /app/node_modules/@prisma/client node_modules/@prisma/client

ENV SUBMISSION_HOST=0.0.0.0 \
    SUBMISSION_PORT=3000

EXPOSE 3000

CMD ["npm", "run", "--workspace", "services/leetcode-submission-service", "submission-server"]
