

## Installation for local development

```bash
brew install fastapi
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e .           # install project + dependencies
pip install -e ".[dev]"    # include dev dependencies
```
