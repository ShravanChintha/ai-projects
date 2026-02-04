def chunk_text(text, chunk_size, overlap=200):
    """
    Splits the input text into chunks of specified size with optional overlap.

    Parameters:
    text (str): The input text to be chunked.
    chunk_size (int): The maximum size of each chunk.
    overlap (int): The number of overlapping characters between consecutive chunks.

    Returns:
    List[str]: A list of text chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def chunk_sentences(sentences, chunk_size, overlap=2):
    """
    Splits a list of sentences into chunks of specified size with optional overlap.

    Parameters:
    sentences (List[str]): The list of sentences to be chunked.
    chunk_size (int): The maximum number of sentences in each chunk.
    overlap (int): The number of overlapping sentences between consecutive chunks.

    Returns:
    List[str]: A list of text chunks formed by joining sentences.
    """
    chunks = []
    start = 0
    total_sentences = len(sentences)

    while start < total_sentences:
        end = min(start + chunk_size, total_sentences)
        chunk = " ".join(sentences[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks
