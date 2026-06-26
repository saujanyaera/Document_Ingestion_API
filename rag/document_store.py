from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

def get_vectorstore(index_name="rag-index"):
    load_dotenv()

    pc = Pinecone()

    # Create index only if it doesn't exist
    existing_indexes = [index["name"] for index in pc.list_indexes()]

    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    embedding = OpenAIEmbeddings()

    vectorstore=PineconeVectorStore(
        index_name=index_name,
        embedding=embedding
    )

    return vectorstore


