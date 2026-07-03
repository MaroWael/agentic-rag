from pathlib import Path
import fitz
from entities.document import Document

class DocumentProcessor:

    def process(self, path: Path) -> list[Document]:
        documents = []
        pdf = fitz.open(path)
        for page_number, page in enumerate(pdf):
            documents.append(
                Document(
                    content=page.get_text(),
                    source=path.name,
                    page=page_number + 1,
                )
            )
        pdf.close()
        return documents