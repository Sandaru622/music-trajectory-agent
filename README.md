# 🎵 Music Trajectory Agent

** Student:** Sandaru Amarasekara
**Student ID:** ITBIN-2313-0008

**Module:** IT41043 – Intelligent Systems
**Faculty:** Faculty of Information Technology, Horizon Campus

**🚀 Live Streamlit Application:**
**https://music-trajectory-agent-asekcppebryfzmqjr6kbty.streamlit.app/**

---
# 🎵 Music Trajectory Agent
## Project Overview

Music Trajectory Agent is an AI-based project developed for the **IT41043 – Intelligent Systems** module.

The system analyzes an artist's music career using a custom music dataset and **Retrieval-Augmented Generation (RAG)**. It combines statistical analysis with AI to generate an easy-to-understand interpretation of an artist's career trajectory.

### How It Works – Two AI Agents

**Trajectory Agent**

* Analyzes the music dataset.
* Calculates artist statistics such as YouTube views and career trends.

**Interpreter Agent**

* Retrieves relevant information from the knowledge base.
* Uses the Groq LLM to generate an AI-powered explanation of the artist's career.

### Supported Artists

* Bathiya & Santhush
* Kasun Kalhara
* Centigradz

> **Note:** The current version of the application supports analysis for **Bathiya & Santhush**, **Kasun Kalhara**, and **Centigradz** only. Additional artists can be added in future by expanding the dataset and rebuilding the vector database.

## Features

- Analyze an artist using a music dataset
- Display artist statistics
- Generate AI-powered career interpretation
- Retrieval-Augmented Generation (RAG)
- Chroma Vector Database
- Knowledge Base Retrieval
- Interactive Streamlit Web Application
- YouTube Views Trend Chart
- Download AI Report

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- LangChain
- ChromaDB
- Groq API
- OpenRouter API
- Sentence Transformers


---

## Project Structure

```
music-trajectory-agent/

agents/
    trajectory_agent.py
    interpreter_agent.py

data/
    songs.csv

knowledge_base/
    music_trends.txt

utils/
    analysis.py
    llm.py
    retriever.py
    vector_store.py
    rag.py

chroma_db/

app.py
requirements.txt
README.md
```

---

## How It Works

1. User enters an artist name.
2. Trajectory Agent analyzes the dataset.
3. Retriever searches the knowledge base.
4. Chroma retrieves relevant documents.
5. Groq LLM combines statistics with retrieved knowledge.
6. Streamlit displays the final report.

---


## AI Agents

### Trajectory Agent

Responsible for:

- Reading the dataset
- Calculating statistics
- Detecting career trends

### Interpreter Agent

Responsible for:

- Retrieving knowledge from ChromaDB
- Using the Groq LLM
- Generating the final AI explanation

---

## RAG Pipeline

User

   │

Streamlit

   │
   
Trajectory Agent

   │ (summary)
   
Retriever (ChromaDB)

   │ (context)
   
Interpreter Agent

   │
   
Groq/OpenRouter

   │
   
Final Report

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/music-trajectory-agent.git
cd music-trajectory-agent
```

### 2. Create a virtual environment (Optional but Recommended)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file or configure **Streamlit Secrets** with your API keys.


```text
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your default browser at:

```
http://localhost:8501
```

## Future Improvements

- Support multiple AI models
- More advanced visualizations
- Music recommendation system
- Spotify API integration

---

## Module

IT41043 – Intelligent Systems

Faculty of Information Technology

Horizon Campus