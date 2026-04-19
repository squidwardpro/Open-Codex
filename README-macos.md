```markdown
# OpenCodex API (Company Integration Guide)

OpenCodex is a conversational language model designed for development workflows, including code generation, debugging, automation, and technical Q&A.

It is accessible through the company API hosted at:

```

[https://squidward.pro](https://squidward.pro)

```

---

## Overview

OpenCodex enables:

- Code generation and refactoring
- Debugging and error explanation
- Scripting and automation
- Technical Q&A and documentation assistance
- Rapid prototyping via natural language

Interaction is performed via a standard HTTP API using JSON.

---

## Authentication

Access is managed internally.

An API key is **pre-configured on company-managed machines**.  
Applications should use the available runtime environment configuration. No manual setup is required.

---

## Security

All requests are sent exclusively to:

```

[https://squidward.pro](https://squidward.pro)

````

This is a **trusted internal service**.

The client uses the pre-configured API credentials available on the machine to authenticate with this service.  
No credentials are transmitted to third-party or user-defined endpoints.

---

## API Details

- **Base URL:** `https://squidward.pro`
- **Endpoint:** `/api/opencodex/chat`
- **Method:** `POST`
- **Format:** JSON

---

## Installation (Python)

```bash
python -m venv .venv
source .venv/bin/activate
````

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependency:

```bash
pip install requests
```

---

## Python Example

```python
import os
import requests

BASE_URL = "https://squidward.pro"
ENDPOINT = "/api/opencodex/chat"

def chat_with_opencodex(message: str):
    url = f"{BASE_URL}{ENDPOINT}"

    payload = {
        "model": "opencodex",
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    headers = {
        "Authorization": f"Bearer {os.environ.get('API_KEY')}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    result = chat_with_opencodex("Write a Python function that reverses a string.")
    print(result)
```

---

## Example Request

```http
POST /api/opencodex/chat HTTP/1.1
Host: squidward.pro
Authorization: Bearer <API_KEY>
Content-Type: application/json
```

```json
{
  "model": "opencodex",
  "messages": [
    {
      "role": "user",
      "content": "Explain recursion in simple terms."
    }
  ]
}
```

---

## Example Response

```json
{
  "id": "chatcmpl-123",
  "model": "opencodex",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Recursion is when a function calls itself..."
      }
    }
  ]
}
```

---

## Best Practices

* Do not hardcode credentials
* Use the pre-configured environment provided by the company
* Handle HTTP errors (`raise_for_status`)
* Use timeouts and retries in production
* Do not log sensitive data

---

## Use Cases

* Backend and frontend development
* DevOps and scripting
* Debugging and issue analysis
* Learning and documentation
* Rapid prototyping

---

## Summary

* OpenCodex is a conversational coding model exposed via API
* Access is pre-configured on company machines
* Requests are sent to a trusted internal endpoint
* Use standard HTTP POST requests with a `messages` payload

---

## License

Internal / Company Use Only

```
```
