

# RAG-LLM-Based InstaChatBot

This project is a Retrieval-Augmented Generation (RAG) chatbot built using Large Language Models (LLMs). It supports JSON dataset ingestion and Instagram data scraping to provide intelligent, context-aware responses.

## 📁 Project Structure
```
Chatbot/
├── db/                                  # Chroma vector store (SQLite DB for embeddings)
│   ├── ee861784-cc0e-4a42-b12f-e6facca47af0/
│   │   └── chroma.sqlite3
│
├── json/                                # Data used for retrieval
│   ├── dataset_with_transcripts.json
│   ├── dataset.json
│   ├── main_dataset.json
│   └── rag_dataset.json
│
├── .env                                 # Environment variables
├── .gitignore
├── config.yaml                          # Configuration file
├── ingest.py                            # Script to load JSON into ChromaDB
├── rag.py                               # Main RAG chatbot logic
├── README.md                            # Project documentation
├── requirements.txt                     # Python dependencies
└── run.bat                              # Optional script to launch the app on Windows
```

---

## ▶️ Getting Started

### 1. Setup Environment

Make sure Python 3.10+ is installed.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file inside the `Chatbot/` folder. Example:

```env
GOOGLE_API_KEY=your_key_here
```
### 4. Run the ingest code
From the `Chatbot/` folder, run

```bash
python ingest.py
```


### 3. Run the Chatbot

From the `Chatbot/` folder, run:

```bash
python rag.py
```

Then open your browser and go to [http://localhost:7860](http://localhost:7860)

> Note: The port may vary if you're using a different Gradio configuration.

---

## 📦 Requirements

* Python 3.10+
* Python packages from `requirements.txt`

Example dependencies:

```txt
python-dotenv
gradio
embedchain
torch 
google-generativeai
```

Generate the list of current dependencies with:

```bash
pip freeze > requirements.txt
```





