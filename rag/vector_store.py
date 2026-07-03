import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from entities.chunk import Chunk

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma")
        self.collection = self.client.get_or_create_collection(
            name="knowledge_base",
            embedding_function=DefaultEmbeddingFunction(),
        )

    def add(self, chunks: list[Chunk]) -> None:
        self.collection.add(
            ids=[chunk.id for chunk in chunks],
            documents=[chunk.content for chunk in chunks],
            metadatas=[
                {
                    "source": chunk.source,
                    "page": chunk.page,
                }
                for chunk in chunks
            ],
        )
        
    def search(
    self,
    query: str,
    top_k: int = 5,
    ) -> list[Chunk]:

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
        )

        chunks = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        ids = results["ids"][0]

        for id_, document, metadata in zip(
            ids,
            documents,
            metadatas,
        ):
            chunks.append(
                Chunk(
                    id=id_,
                    content=document,
                    source=metadata["source"],
                    page=metadata["page"],
                )
            )

        return chunks