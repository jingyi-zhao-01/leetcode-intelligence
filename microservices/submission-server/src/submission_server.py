#!/usr/bin/env python3
"""Minimal TCP submission server entrypoint.

This server is intentionally lightweight so `make submission` has a stable
runtime target while the full microservice is under active development.
"""

from __future__ import annotations

import os
import socketserver

HOST = os.getenv("SUBMISSION_HOST", "0.0.0.0")
PORT = int(os.getenv("SUBMISSION_PORT", "3000"))


class SubmissionTCPHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        data = self.rfile.readline().decode("utf-8", errors="replace").strip()
        if not data:
            return
        response = f"ok: {data}\n"
        self.wfile.write(response.encode("utf-8"))


def run() -> None:
    database_url = os.getenv("DATABASE_URL", "")
    print(f"Submission server listening on {HOST}:{PORT}")
    print(f"DATABASE_URL configured: {'yes' if bool(database_url) else 'no'}")

    with socketserver.ThreadingTCPServer((HOST, PORT), SubmissionTCPHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    run()
