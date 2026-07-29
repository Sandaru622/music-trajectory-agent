# 🎵 Music Trajectory Agent

## Project Overview

Music Trajectory Agent is an Agentic AI application developed for the IT41043 Intelligent Systems module.

The system analyzes an artist's music career using a music dataset and Retrieval-Augmented Generation (RAG). It combines statistical analysis with an AI language model to generate an intelligent interpretation of the artist's career trajectory.

---

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
- LangChain
- ChromaDB
- Groq LLM
- Pandas
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

Knowledge Base

↓

Document Chunking

↓

Embeddings

↓

Chroma Vector Database

↓

Retriever

↓

Groq LLM

↓

Final AI Report

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

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