
# Limitless AI

A self-enhancing AI code generation platform designed to learn through plugins, memory (RAG), and multi-modal feedback.

## Core Features
- Natural language → code generation
- Plugin system for self-expansion
- LangChain + ChromaDB for RAG-based memory
- learn_from_file() to ingest and understand raw content
- Free-tier deployable to Render, HuggingFace, or Fly.io

## Getting Started
1. Install dependencies:
```
pip install -r requirements.txt
```
2. Run the server:
```
uvicorn main:app --reload
```
3. Add plugins to `/plugins/`
4. Learn from files:
```
POST /learn_from_file with a .py, .txt, or .md payload
```

## Deployment Options
- **Render.com**: Create a new web service, auto-deploy from GitHub
- **HuggingFace Spaces**: For frontend + Gradio UI
- **Fly.io**: Use Docker to deploy globally
