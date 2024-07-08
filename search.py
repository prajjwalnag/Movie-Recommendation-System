import psycopg2
import tensorflow as tf
import tensorflow_hub as hub 
import numpy as np
from pgvector.psycopg2 import register_vector
import argparse

if tf.test.is_gpu_available():
    with tf.device('/GPU:0'):
        model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
else:
    with tf.device('/CPU:0'):
        model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Function to convert text to embeddings
def text_to_embeddings(text):
    embeddings = model([text])
    return embeddings

def search_movies_1988():
    parser = argparse.ArgumentParser(description='Search for items based on embeddings.')
    parser.add_argument('--search', type=str, required=True, help='The search term to generate the embedding.')
    args = parser.parse_args()   
    search_phrase=args.search  
    # Register pgvector
    
    #search_phrase="something with a dog or lion"
    embedding =text_to_embeddings(search_phrase)
    embedding=np.array(embedding.numpy().tolist()[0])
    #embedding=embedding.numpy()
    # Connect to PostgreSQL database
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='Rex1993',
        host='localhost',
        port='5432'
        
    )
    cur = conn.cursor()
    register_vector(conn)
    # Query to search for movies released in 1988
    query = "SELECT * FROM movie_plots ORDER BY embedding <-> %s LIMIT 5;"

# Execute the query with the embedding vector
    cur.execute(query, (embedding,))

    # Fetch all results
    movies_1988 = cur.fetchall()

    # Print the results
    for movie in movies_1988:
        print(f"Title: {movie[0]}")
        print(f"Director: {movie[1]}")
        print(f"Cast: {movie[2]}")
        print(f"Genre: {movie[3]}")
        print(f"Plot: {movie[4]}")
        print(f"Year: {movie[5]}")
        print(f"Wiki: {movie[6]}")
        print("-" * 40)

    # Close the connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    search_movies_1988()
