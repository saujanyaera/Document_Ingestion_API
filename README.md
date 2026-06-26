# Document Ingestion API

## Overview

This project is a Document Ingestion API designed for Retrieval Augmented Generation (RAG) pipelines. The API accepts PDF and TXT documents, extracts content and metadata, applies configurable text chunking strategies, generates vector embeddings, stores embeddings in Pinecone, and saves document metadata in a MySQL database.

## Features

Upload PDF Documents
Extract document text and metadata
Support multiple chunking strategies:

  Recursive Character Text Splitter
  Character Text Splitter

Generate embeddings using Large Language Model embedding APIs
Store vector embeddings in Pinecone
Store document metadata in MySQL
Modular pipeline architecture for easy extension

## Architecture

Document Upload
→ Text Extraction
→ Metadata Extraction
→ Chunking
→ Embedding Generation
→ Pinecone Vector Storage
→ MySQL Metadata Storage

## Metadata Stored

The following metadata fields are extracted and stored in MySQL:

| Field   | Description                             |
| ------- | --------------------------------------- |
| Author  | Document author                         |
| Creator | Application used to create the document |
| Page    | Page number associated with the chunk   |

## Chunking Strategies

### Recursive Character Text Splitter

This strategy recursively splits text while attempting to preserve semantic structure by using separators such as paragraphs, sentences, and spaces before falling back to character-level splitting.

### Character Text Splitter

This strategy splits text strictly based on character count and overlap configuration.

## Technologies Used

### Backend

Python
Flask

### Vector Database

Pinecone

### Database

MySQL
SQLAlchemy ORM

### Document Processing

* PyPDF
* LangChain Text Splitters

### Embeddings

* OpenAI Embeddings

## Project Structure

```text
ASSIGNMENT_1/
│
├── app.py
     |──config.py

├── routes.py
├──services/
│   └── pipeline.py
│
├── rag/
│   ├── document_ingestion.py
│   ├── document_splitting.py
│   └── document_store.py
│
├── database/
│   └── metadata.py
│
├── uploads/
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Environment Variables

Create a `.env` file using the `.env.example` template.

env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key

DB_USER=username
DB_PASSWORD=password
DB_HOST=localhost
DB_NAME=metadata

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd ASSIGNMENT_1
```

Create a virtual environment:

```bash
python -m venv env
```

Activate the virtual environment:

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The API will start locally and accept document uploads through the configured endpoint.

## Workflow

1. Upload a PDF or TXT file.
2. Extract document text and metadata.
3. Select a chunking strategy.
4. Generate embeddings for each chunk.
5. Store embeddings in Pinecone.
6. Store metadata in MySQL.
7. Return ingestion status and document information.



## Author

Saujanya Bhattarai
