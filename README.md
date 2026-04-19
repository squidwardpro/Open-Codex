```markdown
# OpenCodex API (Company Integration Guide)

OpenCodex is a conversational language model designed to help developers and teams write code, debug issues, generate ideas, and interact with software systems using natural language.

It is available internally through the company API hosted at:

```

[https://squidward.pro](https://squidward.pro)

````

This guide provides a simple Python-based setup for interacting with OpenCodex.

---

## Overview

OpenCodex allows you to:

- Generate and review code
- Debug errors and explain stack traces
- Automate repetitive development tasks
- Prototype ideas quickly using natural language
- Ask technical questions and get contextual answers

It works via a standard HTTP API where you send messages and receive responses from the model.

---

## Authentication

Access to OpenCodex is managed internally.

Your API key is **pre-configured on your work machine by the company**.  
You do not need to request or manually set up credentials.

Applications and scripts should simply use the available environment configuration at runtime.  
No additional setup is required.

---

## API Details

- **Base URL:** `https://squidward.pro`
- **Endpoint:** `/api/opencodex/chat`
- **Method:** `POST`
- **Format:** JSON

---

## Installation (Python)

Set up a clean Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
````

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install required dependency:

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

    # The API key is already available via the environment on your machine
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

* Do not hardcode credentials in source code
* Rely on the environment configuration provided by the company
* Handle API errors gracefully
* Use timeouts and retries in production systems
* Avoid logging sensitive data

---

## Use Cases

OpenCodex is especially useful for:

* Backend and frontend development
* DevOps automation
* Writing scripts and utilities
* Learning new frameworks or languages
* Rapid prototyping

---

## Summary

* OpenCodex is a conversational coding assistant available via API
* Access is already configured on your machine
* Use standard HTTP requests to interact with the model
* Send messages, receive responses, and integrate into your workflows

---

## License

Internal / Company Use Only

```
```
