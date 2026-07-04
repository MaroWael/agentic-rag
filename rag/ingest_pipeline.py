from pathlib import Path

from rag.document_processor import DocumentProcessor
from rag.text_chunker import TextChunker
from rag.vector_store import VectorStore


class IngestPipeline:

    def __init__(self):
        self.processor = DocumentProcessor()
        self.chunker = TextChunker()
        self.vector_store = VectorStore()

    def ingest(self, folder: Path) -> None:
        all_chunks = []
        for pdf_file in folder.glob("*.pdf"):
            print(f"Processing {pdf_file.name}")
            documents = self.processor.process(pdf_file)
            for document in documents:
                chunks = self.chunker.chunk(document)
                all_chunks.extend(chunks)
        self.vector_store.add(all_chunks)
        print(f"\nIndexed {len(all_chunks)} chunks.")