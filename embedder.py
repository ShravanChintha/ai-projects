from sentence_transformers import SentenceTransformer
from chunk import chunk_text, chunk_sentences
from pdf_loader import load_pdf
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def get_embeddings(model_name, chunks):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks)
    return embeddings


pages_text, full_text = load_pdf("vl-jepa.pdf")
text_chunks = chunk_text(full_text, chunk_size=1000, overlap=200)

embeddings = get_embeddings('all-MiniLM-L6-v2', text_chunks)
print(f"Generated {len(embeddings)} embeddings for {len(text_chunks)} text chunks, with shape {embeddings.shape}.")

embeddings_model2 = get_embeddings('all-mpnet-base-v2', text_chunks)
print(f"Generated {len(embeddings_model2)} embeddings for {len(text_chunks)} text chunks, with shape {embeddings_model2.shape}.")
