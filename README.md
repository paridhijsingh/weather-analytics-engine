# Weather Analytics Engine & AI Agent 🚀

A containerized, asynchronous FastAPI application that integrates real-time environmental data with Large Language Model (LLM) reasoning to provide contextual life advice.

## 🌟 Key Features

- **Asynchronous Data Ingestion:** Uses `httpx` to fetch real-time data from the OpenWeather API.
- **Agentic Reasoning Layer:** Integrated **OpenAI GPT-4o** to transform raw temperature data into personalized, actionable recommendations.
- **Relational Persistence:** Implements **SQLAlchemy ORM** to log weather trends into a SQLite database for longitudinal statistical analysis.
- **Production-Ready Architecture:** Fully containerized using **Docker** for consistent deployment and scalability.

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, FastAPI
- **AI/ML:** OpenAI API (GPT-4o), Prompt Engineering
- **Database:** SQLite, SQLAlchemy
- **DevOps:** Docker, Git, Dotenv

## 🚀 Getting Started

1. **Clone the repository**
2. **Setup environment variables:** Create a `.env` file and add your `OPENAI_API_KEY`.
3. **Build and Run with Docker:**
   ```bash
   docker build -t weather-agent .
   docker run -p 8000:8000 weather-agent
   ```
