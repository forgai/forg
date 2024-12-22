# Forg Python SDK

[![PyPI version](https://img.shields.io/pypi/v/forg.svg)](https://pypi.org/project/forgai)

The Forg Python SDK provides convenient access to the Forg REST API from any Python 3.8+
application. The SDK includes rich type definitions and enables receiving real-time executions
via WebSockets.

## Documentation

Full documentation of the SDK is available at [https://forg.ai/docs/sdk/introduction](https://forg.ai/docs/sdk/introduction). You may also want to check out the [REST API Reference](https://forg.ai/docs/api/v1/introduction).

## Installation

You can install the SDK via `pip`:

```bash
pip install forgai```

## Usage

Once installed, you can use it to make requests.

### Create an Agent

```python
import forgai
forg.api_key = "YOUR_API_KEY"

agent = forg.Agent.create(
    name="My Agent",
    script="def main(request):\n    return request.payload",
    requirements="requests==2.31.0\npandas==2.1.4",
    env_vars="FOO=bar\nBAZ=qux",
    python_version="3.11",
)
```

### Execute an Agent

```python
import forgai
forg.api_key = "YOUR_API_KEY"

agent = forg.Agent.retrieve(id="15d19ca3-26f1-4adb-9cea-3955b73d9b4e")

execution = agent.execute(payload={"key": "value"})
```

These are only a few examples of what you can do with the SDK. Refer to the [full documentation](https://forg.ai/docs/sdk/introduction) to learn more about the SDK.
