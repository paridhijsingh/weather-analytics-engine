# Weather Analytics Engine & AI Advisor

An asynchronous FastAPI service that fetches real-time weather data, stores it in a SQLite database for longitudinal analysis, and provides "agentic" recommendations based on current conditions.

## 🚀 Features

- **Asynchronous API:** Built with FastAPI and `httpx` for high-performance data retrieval.
- **Relational Storage:** SQLAlchemy ORM used to log weather patterns for future data science tasks.
- **AI Reasoning:** Context-aware logic layer that simulates "Agentic" decision-making.
- **Containerized:** Fully Dockerized for consistent deployment across environments.

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Pydantic
- **Data:** SQLAlchemy, SQLite
- **DevOps:** Docker, httpx
- **Stats/Analysis:** Python-based aggregation of weather trends

## 📦 Getting Started

1. Clone the repo.
2. Build the container: `docker build -t weather-engine .`
3. Run: `docker run -p 8000:8000 weather-engine`
