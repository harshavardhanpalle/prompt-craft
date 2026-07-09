# Prompt Optimizer 🚀

An AI-powered Chrome extension that optimizes user prompts before sending them to AI models.

The goal is to reduce unnecessary words, preserve user intent, improve prompt clarity, and reduce token usage.


## Problem Statement

Users often write long, conversational prompts. For example:

> hey can you please explain kubernetes because i am new to devops and want to understand everything in detail

The optimizer converts it into:

> Explain Kubernetes for a DevOps beginner, including detailed information.

---

## Architecture

```
User
  ↓
Chrome Extension
  ↓
FastAPI Backend
  ↓
Ollama (Local LLM)
  ↓
Optimized Prompt
```

---

## Features

### Current MVP
- Chrome Extension UI
- Prompt input
- AI prompt optimization
- Local LLM inference
- FastAPI REST API
- Prompt length comparison
- Token reduction percentage

### Future Improvements
- Direct integration with ChatGPT/Gemini textbox
- Automatic prompt optimization
- Prompt history
- User accounts
- Cloud deployment
- Multiple AI model support

---

## Tech Stack

**Frontend:** Chrome Extension (Manifest V3), HTML, CSS, JavaScript

**Backend:** Python, FastAPI, Pydantic

**AI:** Ollama, Qwen models

---

## Project Structure

```
prompt-optimizer/
├── backend/      FastAPI application
├── extension/    Chrome browser extension
└── docs/         Architecture documentation
```

---

## Local Setup

### 1. Start Ollama

Install Ollama from [ollama.com](https://ollama.com), then:

```bash
ollama serve
ollama run qwen2.5:1.5b
```

### 2. Start the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- Backend: `http://localhost:8000`
- Swagger docs: `http://localhost:8000/docs`

### 3. Load the Chrome Extension

1. Open `chrome://extensions`
2. Enable **Developer Mode**
3. Click **Load unpacked**
4. Select the `extension/` folder

---

## API Documentation

### `POST /api/optimize`

**Request**
```json
{
  "prompt": "Explain Kubernetes"
}
```

**Response**
```json
{
  "optimized_prompt": "Explain Kubernetes architecture.",
  "original_length": 3,
  "optimized_length": 2,
  "token_reduction_percentage": 33.33
}
```

---

## Development Flow

```
User Prompt → Chrome Extension → FastAPI API → Ollama Model → Optimized Prompt
```

---

## Project Status

**Current version:** MVP v1.0
**Built with:** Chrome Extension + FastAPI + Ollama + Local LLM

---

## License

MIT © Harsha Palle — see [LICENSE](LICENSE) for details.
