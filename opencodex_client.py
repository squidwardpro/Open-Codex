#!/usr/bin/env python3
"""
OpenCodex client for squidward.pro

What this script does:
- Reads the pre-configured API key from ~/env
- Accepts either:
  - a raw key in ~/env
  - or KEY=VALUE style lines in ~/env
- Sends a POST request to the OpenCodex chat endpoint
- Prints the JSON response

Usage:
    python opencodex_client.py "Explain recursion simply"

Optional:
    python opencodex_client.py --env-file ~/env "Write a Python sorting function"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import requests


BASE_URL = "https://squidward.pro"
ENDPOINT = "/api/opencodex/chat"
DEFAULT_ENV_FILE = "~/env"


def load_api_key(env_file: str) -> str:
    """
    Load the API key from the given env file.

    Supported formats:
    1. Raw token only:
         sk-abc123
    2. KEY=VALUE format:
         API_KEY=sk-abc123
         OPENCODEX_KEY=sk-abc123
    3. export KEY=VALUE format:
         export API_KEY=sk-abc123
    """
    path = Path(env_file).expanduser()

    if not path.exists():
        raise FileNotFoundError(f"Environment file not found: {path}")

    text = path.read_text(encoding="utf-8").strip()

    if not text:
        raise RuntimeError(f"Environment file is empty: {path}")

    # If the whole file is just a raw token, use it directly.
    if "\n" not in text and "=" not in text and " " not in text:
        return text.strip().strip('"').strip("'")

    # Otherwise, inspect lines and use the first non-empty value we can parse.
    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("export "):
            line = line[len("export "):].strip()

        if "=" in line:
            _, value = line.split("=", 1)
            value = value.strip().strip('"').strip("'")
            if value:
                return value

        # Fallback: if a non-empty line has no "=", treat it as the key.
        if line:
            return line.strip().strip('"').strip("'")

    raise RuntimeError(f"Could not parse an API key from: {path}")


def chat_with_opencodex(message: str, api_key: str) -> dict:
    url = f"{BASE_URL}{ENDPOINT}"

    payload = {
        "model": "opencodex",
        "messages": [
            {"role": "user", "content": message}
        ],
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Talk to OpenCodex using the API key already stored in ~/env."
    )
    parser.add_argument(
        "message",
        nargs="+",
        help="Message to send to OpenCodex",
    )
    parser.add_argument(
        "--env-file",
        default=DEFAULT_ENV_FILE,
        help="Path to the file containing the pre-configured API key (default: ~/env)",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the JSON response",
    )

    args = parser.parse_args()
    prompt = " ".join(args.message)

    try:
        api_key = load_api_key(args.env_file)

        # Make it available in-process for any downstream code that expects ENV.
        os.environ["API_KEY"] = api_key

        result = chat_with_opencodex(prompt, api_key)

        if args.pretty:
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(result))

        return 0

    except requests.HTTPError as exc:
        print(f"HTTP error: {exc}", file=sys.stderr)
        if exc.response is not None:
            try:
                print(exc.response.text, file=sys.stderr)
            except Exception:
                pass
        return 1
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
