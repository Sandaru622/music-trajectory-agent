# 🎵 Music Trajectory Agent

**Student:** Sandaru Pradeepthi Amarasekara  
**Student ID:** ITBIN-2313-0008  

**Module:** IT41043 – Intelligent Systems  
**Faculty:** Faculty of Information Technology, Horizon Campus  

## 🚀 Live Streamlit Application

https://music-trajectory-agent-asekcppebryfzmqjr6kbty.streamlit.app/

---

# Project Overview

Music Trajectory Agent is an AI-based project developed for the **IT41043 – Intelligent Systems** module.

The system analyzes an artist's music career using a custom music dataset and **Retrieval-Augmented Generation (RAG)**. It combines statistical analysis with AI to generate an easy-to-understand interpretation of an artist's career trajectory.

## How It Works – Two AI Agents

### Trajectory Agent

- Analyzes the music dataset.
- Calculates artist statistics such as YouTube views and career trends.

### Interpreter Agent

- Retrieves relevant information from the knowledge base.
- Uses the Groq LLM to generate an AI-powered explanation of the artist's career.

## Supported Artists

- Bathiya & Santhush
- Kasun Kalhara
- Centigradz

> **Note:** The current version supports only these three artists. More artists can be added in future by expanding the dataset and rebuilding the vector database.

---

# Features

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

# Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- LangChain
- ChromaDB
- Sentence Transformers
- Groq API
- OpenRouter API

---

# Known Limitations

- Supports only three artists.
- Dataset is manually created.
- Knowledge base is limited.
- Uses YouTube popularity data only.

---

# Project Structure

```text
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
    openrouter_llm.py
    retriever.py
    vector_store.py
    rag.py

chroma_db/

app.py
requirements.txt
README.md
```

---

# How It Works

1. User enters an artist name.
2. Trajectory Agent analyzes the dataset.
3. Retriever searches the knowledge base.
4. Chroma retrieves relevant documents.
5. Groq LLM combines statistics with retrieved knowledge.
6. Streamlit displays the final AI report.

---

# Agent Communication Diagram

```text
+--------+
|  User  |
+--------+
     |
     v
+------------------+
| Trajectory Agent |
+------------------+
     |
     | Artist Summary
     v
+-------------------+
| Interpreter Agent |
+-------------------+
     |
     | Retrieved Context
     v
+------------------+
| Groq/OpenRouter  |
+------------------+
     |
     v
+------------------+
|  Final Response  |
+------------------+
```

---

# AI Agents

## Trajectory Agent

Responsible for:

- Reading the dataset
- Calculating statistics
- Detecting career trends

## Interpreter Agent

Responsible for:

- Retrieving knowledge from ChromaDB
- Using the Groq LLM
- Generating the final AI explanation

---

# Architecture Diagram

```text
+--------+
|  User  |
+--------+
     |
     v
+----------------+
|   Streamlit    |
+----------------+
     |
     v
+------------------+
| Trajectory Agent |
+------------------+
     |
     | Summary
     v
+----------------------+
| Retriever (ChromaDB) |
+----------------------+
     |
     | Context
     v
+-------------------+
| Interpreter Agent |
+-------------------+
     |
     v
+------------------+
| Groq/OpenRouter  |
+------------------+
     |
     v
+------------------+
|  Final AI Report |
+------------------+
```

---

# RAG Pipeline Explanation

The knowledge base is split into smaller chunks using LangChain's RecursiveCharacterTextSplitter. The chunks are converted into vector embeddings using Sentence Transformers and stored in ChromaDB. When a user searches for an artist, the Retriever finds the most relevant knowledge, which is combined with artist statistics by the LLM to generate the final AI report.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/music-trajectory-agent.git
cd music-trajectory-agent
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure API Keys

Create a `.env` file.

```text
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

## 5. Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# Future Improvements

- Support more artists
- Support multiple AI models
- Improve data visualizations
- Spotify API integration
- Music recommendation system
- Automatic dataset updates