from pypdf import PdfReader
from chunk import chunk_text, chunk_sentences

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    # return page numbers and text
    pages_text = []
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text() or ""
        pages_text.append((i + 1, page_text))
        text += page_text + "\n"
    return pages_text, text