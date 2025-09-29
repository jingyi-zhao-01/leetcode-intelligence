import os
from typing import Optional

from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.openai import OpenAI

# Load environment variables from .env file
load_dotenv()


def build_index(doc_path: str):
    docs = SimpleDirectoryReader(input_files=[doc_path]).load_data()
    llm_api_key = os.getenv("OPENAI_API_KEY")
    if not llm_api_key:
        raise RuntimeError(
            "Please set OPENAI_API_KEY in your environment to use OpenAI LLM."
        )
    Settings.llm = OpenAI(model="gpt-5")
    index = VectorStoreIndex.from_documents(docs)
    return index


def ask(index, question: str) -> str:
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return str(response)


def main(argv: Optional[list[str]] = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Ask questions about a local document using LlamaIndex"
    )
    parser.add_argument("file", help="Path to a .txt document")
    parser.add_argument(
        "question", nargs="*", help="Question to ask about the document"
    )
    args = parser.parse_args(argv)

    q = " ".join(args.question) if args.question else "What is this document about?"
    index = build_index(args.file)
    answer = ask(index, q)
    print(answer)


if __name__ == "__main__":
    main()
