# query the collection and get similar chunks based on a query amd their scores
import chromadb 
from chromadb import Search, K, Knn
from embedder import get_embeddings
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="pdf_embeddings") 
def query_collection(query, top_k=5):
    # Get embedding for the query
    query_embedding = get_embeddings('all-MiniLM-L6-v2', [query])[0]

    # Query the collection for similar chunks
    # Note: ChromaDB 'where' filters on metadata, not distance scores. Filtering by distance must be done on the results.
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results

# Example usage
if __name__ == '__main__':
    user_query = "what can I infer from vision transformers?"
    results = query_collection(user_query)
    #filter the results based on distance scores to get the top_k most similar chunks
    filtered_results = {
        'documents': [],
        'metadatas': [],
        'distances': []
    }
    for doc, meta, dist in zip(results['documents'][0], results['metadatas'][0], results['distances'][0]):
        if dist < 1.15:  # Adjust the threshold as needed
            filtered_results['documents'].append(doc)
            filtered_results['metadatas'].append(meta)
            filtered_results['distances'].append(dist)
    print("Top similar chunks:")
    for doc, meta, dist in zip(filtered_results['documents'], filtered_results['metadatas'], filtered_results['distances']):
        print(f"Chunk: {doc}\nMetadata: {meta}\nDistance: {dist}\n")