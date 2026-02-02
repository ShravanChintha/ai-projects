from pypdf import PdfReader

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

# Example usage:
pages_text, full_text = load_pdf("vl-jepa.pdf")
for page_num, page_text in pages_text:
    print(f"Page {page_num}:\n{page_text}\n")