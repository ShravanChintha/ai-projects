from sentence_transformers import SentenceTransformer

def get_embeddings(model_name, chunks):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks)
    return embeddings