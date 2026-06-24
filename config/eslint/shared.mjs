import path from 'node:path';
import { fileURLToPath } from 'node:url';

import { FlatCompat } from '@eslint/eslintrc';
import js from '@eslint/js';
import { defineConfig, globalIgnores } from 'eslint/config';
import globals from 'globals';
import tseslint from 'typescript-eslint';

export const sharedIgnores = [
  '**/node_modules/**',
  '**/dist/**',
  '**/build/**',
  '**/.venv/**',
  '**/__pycache__/**',
  'services/**/generated/**',
  'services/**/coverage/**',
];

export function moduleDir(importMetaUrl) {
  return path.dirname(fileURLToPath(importMetaUrl));
}

export function createServiceLintConfig({ serviceFiles, testFiles = [] }) {
  const config = [
    {
      ignores: sharedIgnores,
    },
    {
      files: serviceFiles,
      extends: [js.configs.recommended, ...tseslint.configs.recommended],
      languageOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        globals: {
          ...globals.node,
        },
      },
      rules: {
        'no-console': 'off',
        '@typescript-eslint/no-explicit-any': 'off',
        '@typescript-eslint/no-unused-vars': [
          'error',
          {
            argsIgnorePattern: '^_',
            varsIgnorePattern: '^_',
            caughtErrorsIgnorePattern: '^_',
          },
        ],
      },
    },
  ];

  if (testFiles.length > 0) {
    config.push({
      files: testFiles,
      languageOptions: {
        globals: {
          ...globals.node,
          ...globals.vitest,
        },
      },
    });
  }

  return tseslint.config(...config);
}

export function createNextClientLintConfig(baseDirectory) {
  const compat = new FlatCompat({ baseDirectory });

  return defineConfig([
    ...compat.extends('next/core-web-vitals'),
    globalIgnores([...sharedIgnores, '.next/**', 'out/**', 'build/**', 'next-env.d.ts']),
  ]);
}
