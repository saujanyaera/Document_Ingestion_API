from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings()

def docs_splitter_recursive(docs):
    splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
    )

    return splitter.split_documents(docs)

# def docs_splitter_semantic(docs):
#     splitter=SemanticChunker(
#         embedding=embeddings,
#         breakpoint_threshold_types='standard_deviation',
#         breakpoint_threshold_Amount=95
#     )
    # return splitter.create_documents(docs)


