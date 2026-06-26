from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from typing import Literal

load_dotenv()

embeddings=OpenAIEmbeddings()

def docs_splitter_recursive(docs, strategy: Literal['recursive', 'character']='recursive'):
    if strategy=="recursive":
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20
        )
        return splitter.split_documents(docs)

    elif strategy=="character":
        splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
    )

        chunks = splitter.split_documents(docs)
        return chunks

    else:
        raise ValueError("Invalid chunking strategy")


