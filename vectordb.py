import chromadb
from pdf_loader import load_pdf
from chunk import chunk_text
from embedder import get_embeddings

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="pdf_embeddings")

# function to process PDF, chunk it, get embeddings and store in ChromaDB 
def process_pdf(file_path, chunk_size=1000, overlap=200):
    # Load PDF content
    # load_pdf returns (pages_list, full_text_string), so we unpack it
    _, text = load_pdf(file_path)

    # Chunk the text
    chunks = chunk_text(text, chunk_size, overlap)

    # Get embeddings for each chunk
    embeddings = get_embeddings('all-MiniLM-L6-v2', chunks)

    # Store chunks and embeddings in ChromaDB
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            ids=[f"chunk_{i}"],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{"source": file_path, "chunk_index": i}]
        )

# Example usage
if __name__ == '__main__':
    # check if this collection is already populated to avoid re-processing the PDF every time we run the script
    if collection.count() == 0:
        pdf_file = "vl-jepa.pdf"
        process_pdf(pdf_file)
        print(f"Processed and stored chunks from {pdf_file} in ChromaDB.")
    else:
        print("Collection already populated. Skipping PDF processing.")
    print(f"Total documents in collection: {collection.count()}")
    print(f"Sample document from collection: {collection.peek(1)}")
