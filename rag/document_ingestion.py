from langchain_community.document_loaders import PyPDFLoader
import os


def docs_loader(filename):

    loader=PyPDFLoader(filename)
    docs=loader.load()
    return docs

# result=docs_loader('saujanyacv2026.pdf')
# print(result)



