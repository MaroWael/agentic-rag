import tiktoken

from entities.chunk import Chunk
from entities.document import Document


class TextChunker:
    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50,
    ):
        self.encoding = tiktoken.get_encoding("cl100k_base")
        self.chunk_size = chunk_size
        self.overlap = overlap
    import tiktoken

from entities.chunk import Chunk
from entities.document import Document


class TextChunker:
    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50,
    ):
        self.encoding = tiktoken.get_encoding("cl100k_base")
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: Document) -> list[Chunk]:
        tokens = self.encoding.encode(document.content)
        chunks = []
        start = 0
        chunk_number = 0

        while start < len(tokens):
            end = start + self.chunk_size
            chunk_tokens = tokens[start:end]
            chunk_text = self.encoding.decode(chunk_tokens)

            chunks.append(
                Chunk(
                    id=f"{document.source}_{document.page}_{chunk_number}",
                    content=chunk_text,
                    source=document.source,
                    page=document.page,
                )
            )
            chunk_number += 1
            start += self.chunk_size - self.overlap
        return chunks