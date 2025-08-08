# ChatGPT Clone Skeleton

This repository contains a minimal skeleton for a ChatGPT-like application
using **React** for the frontend and **Django** for the backend with SQL
persistence. A placeholder custom LLM echoes user input.

## Structure

- `backend/` – Django project with REST endpoint `/api/chat/`.
- `frontend/` – Simple React UI using CDN scripts.
- `requirements.txt` – Python dependencies for the backend.

## Running

Dependencies cannot be installed in this environment, but locally you would run:

```bash
pip install -r requirements.txt
python backend/manage.py migrate
python backend/manage.py runserver
```

Then open `frontend/index.html` in a browser to use the chat interface.
