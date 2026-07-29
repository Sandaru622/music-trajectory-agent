# 🎵 Music Trajectory Agent

## Project Overview
This is an AI-based project made for the IT41043 – Intelligent Systems module. It looks at an artist's music career using a music dataset and a technique called RAG (Retrieval-Augmented Generation). It mixes number-based analysis with AI to explain how an artist's career has grown or changed over time.

How it works - Two AI Agents

 Trajectory Agent - Looks at the music data and calculates statistics about the artist (like views, streams, trends,etc.)
 Interpreter Agent - Finds useful information from the knowledge base and uses the Groq LLM (AI model) to write a   clear,easy-to-understand explanation of the artist's career.

Artists supported right now:
-  Bathiya & Santhush
-  Kasun Kalhara
-  Centigradz


> **Note:** The current version of the application supports analysis for **Kasun Kalhara**, **Bathiya & Santhush**, and **Centigradz** only. Additional artists can be added in future by expanding the dataset and rebuilding the vector database.


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

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
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