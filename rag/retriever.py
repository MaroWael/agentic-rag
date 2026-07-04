from rag.vector_store import VectorStore

class Retriever:
    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> str:
        chunks = self.vector_store.search(
            query=query,
            top_k=top_k,
        )
        context = []
        for chunk in chunks:
            context.append(
                f"""
                Source: {chunk.source}
                Page: {chunk.page}
                {chunk.content}
                """
            )
        return "\n\n".join(context)