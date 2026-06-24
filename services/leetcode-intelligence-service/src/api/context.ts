import type { PrismaClient } from '@prisma/client';

export type ApiContext = {
  prisma: PrismaClient;
};
