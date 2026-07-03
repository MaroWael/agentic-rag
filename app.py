from pathlib import Path

from rag.document_processor import DocumentProcessor
from rag.text_chunker import TextChunker
from rag.vector_store import VectorStore

processor = DocumentProcessor()
chunker = TextChunker(chunk_size=100, overlap=20)
vector_store = VectorStore()

documents = processor.process(Path("library/ml.pdf"))

all_chunks = []

for document in documents:
    all_chunks.extend(
        chunker.chunk(document)
    )

vector_store.add(all_chunks)

print(f"Stored {len(all_chunks)} chunks.")

results = vector_store.search(
    "What is Reinforcement learning?"
)

print(results)