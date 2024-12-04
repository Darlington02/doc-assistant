from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def ingest_docs():
    loader = ReadTheDocsLoader("/Users/darlingtonnnam/Desktop/programming/Python:Langchain/documentation-helper/langchain-docs/api.python.langchain.com/en/latest")

    raw_docunents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_docunents)
    
    for doc in documents:
        new_url = doc.metadata["source"]
        new_url = new_url.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"going to add {len(documents)} to Pinecone")

    PineconeVectorStore.from_documents(
        documents, embeddings, index_name="langchain-doc-index"
    )

    print(f"***Loading to Pinecone done***")

if __name__ == "__main__":
    ingest_docs()