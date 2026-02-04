from pypdf import PdfReader
from chunk import chunk_text, chunk_sentences

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    # return page numbers and text
    pages_text = []
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        pages_text.append((i + 1, page_text))
        text += page_text + "\n"
    return pages_text, text

pages_text, full_text = load_pdf("vl-jepa.pdf")

# Example usage of chunking functions
text_chunks = chunk_text(full_text, chunk_size=1000, overlap=200)
sentences = full_text.split('. ')
sentence_chunks = chunk_sentences(sentences, chunk_size=5, overlap=2)
print(f"Total pages: {len(pages_text)}")
print(f"Total text chunks: {len(text_chunks)}") 
print(f"Total sentence chunks: {len(sentence_chunks)}")
print("sentence_chunks:", sentence_chunks)