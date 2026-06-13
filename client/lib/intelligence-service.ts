import 'server-only';

function getBaseUrl() {
  const value = process.env.BFF_SERVICE_URL?.trim();
  if (!value) {
    throw new Error('BFF_SERVICE_URL is required.');
  }

  return value.replace(/\/+$/, '');
}

function getToken() {
  const value = process.env.BFF_TOKEN?.trim();
  if (!value) {
    throw new Error('BFF_TOKEN is required.');
  }

  return value;
}

type RequestOptions = {
  method?: 'GET' | 'POST' | 'DELETE';
  body?: unknown;
};

export async function getIntelligenceServiceJson<T>(path: string, options: RequestOptions = {}): Promise<T> {
  const response = await fetch(`${getBaseUrl()}${path}`, {
    method: options.method ?? 'GET',
    headers: {
      Authorization: `Bearer ${getToken()}`,
      'Content-Type': 'application/json',
    },
    body: options.body === undefined ? undefined : JSON.stringify(options.body),
    cache: 'no-store',
  });

  if (!response.ok) {
    let message = `${response.status} ${response.statusText}`;
    try {
      const payload = (await response.json()) as { error?: string };
      if (payload.error) {
        message = payload.error;
      }
    } catch {
      // ignore JSON parse failure and keep HTTP status text
    }
    throw new Error(message);
  }

  return response.json() as Promise<T>;
}
