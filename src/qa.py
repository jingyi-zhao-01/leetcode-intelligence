import os
import argparse
from typing import Optional
from pathlib import Path

from dotenv import load_dotenv
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    Settings,
    StorageContext,
)
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

# Load environment variables from .env file
load_dotenv()


SUBMISSION_DIR = Path(__file__).resolve().parents[1] / "submissions"
PERSIST_DIR = Path(__file__).resolve().parents[1] / ".vector_storage"


def build_index():
    """Build or load the vector index with ChromaDB persistent storage."""
    # Configure API key and settings first
    llm_api_key = os.getenv("OPENAI_API_KEY")
    if not llm_api_key:
        raise RuntimeError(
            "Please set OPENAI_API_KEY in your environment to use OpenAI LLM."
        )

    Settings.llm = OpenAI(model="gpt-5")
    Settings.embed_model = OpenAIEmbedding()

    # Create ChromaDB client with persistent storage
    PERSIST_DIR.mkdir(exist_ok=True)
    chroma_client = chromadb.PersistentClient(path=str(PERSIST_DIR))

    # Get or create collection
    collection_name = "leetcode_submissions"
    try:
        chroma_collection = chroma_client.get_collection(collection_name)
        print(f"Loading existing ChromaDB collection '{collection_name}'...")

        # Create vector store from existing collection
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # Load index from vector store
        index = VectorStoreIndex.from_vector_store(
            vector_store=vector_store, storage_context=storage_context
        )
        print("Existing ChromaDB index loaded successfully!")
        return index

    except Exception as e:
        print(f"Collection doesn't exist or failed to load: {e}")
        print("Building new ChromaDB index...")

        # Create new collection
        chroma_collection = chroma_client.create_collection(collection_name)

        # Read documents
        print("Reading documents...")
        reader = SimpleDirectoryReader(input_dir=SUBMISSION_DIR)
        docs = reader.load_data(num_workers=4)

        # Create vector store
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # Build index with ChromaDB
        print("Building vector index with ChromaDB...")
        index = VectorStoreIndex.from_documents(
            docs, storage_context=storage_context, show_progress=True
        )

        print(f"ChromaDB index saved to {PERSIST_DIR}")
        return index


def ask(index, question: str, streaming: bool = False) -> str:
    """Query the index using the recommended LlamaIndex pattern."""
    if streaming:
        query_engine = index.as_query_engine(streaming=True)
        streaming_response = query_engine.query(question)
        # Collect the streaming response into a string
        response_text = ""
        for text in streaming_response.response_gen:
            response_text += text
        return response_text
    else:
        query_engine = index.as_query_engine()
        response = query_engine.query(question)
        return str(response)


def main(streaming: bool = False) -> None:
    print("Building index from LeetCode submissions...")
    index = build_index()
    print("Index built successfully! Ready to answer questions.\n")

    print("Interactive LeetCode Q&A System")
    if streaming:
        print("Streaming mode enabled - responses will stream in real-time")
    print("Type 'quit', 'exit', or 'q' to exit")
    print("-" * 50)

    while True:
        try:
            query = input("\nEnter your question: ").strip()

            if query.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            if not query:
                print("Please enter a question.")
                continue

            if streaming:
                print("\nThinking...")
                # Use streaming pattern
                query_engine = index.as_query_engine(streaming=True)
                streaming_response = query_engine.query(query)
                print("\nAnswer: ", end="", flush=True)
                streaming_response.print_response_stream()
                print()  # Add newline after streaming
            else:
                print("\nThinking...")
                answer = ask(index, query, streaming=False)
                print(f"\nAnswer: {answer}")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again with a different question.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Interactive LeetCode Q&A system using LlamaIndex"
    )
    parser.add_argument(
        "--streaming",
        "-s",
        action="store_true",
        help="Enable streaming responses for real-time output",
    )
    args = parser.parse_args()

    # Interactive mode with optional streaming
    main(streaming=args.streaming)
