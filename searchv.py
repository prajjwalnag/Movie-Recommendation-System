import psycopg2
import tensorflow as tf
import tensorflow_hub as hub 
import numpy as np
from pgvector.psycopg2 import register_vector

model = None

def init():
    global model
    # Load the model
    if tf.test.is_gpu_available():
        with tf.device('/GPU:0'):
            model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    else:
        with tf.device('/CPU:0'):
            model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    print("Model Intialized")

# Function to convert text to embeddings
def text_to_embeddings(text):
    embeddings = model([text])
    return embeddings

def search_items(search_term):
    embedding = text_to_embeddings(search_term)
    embedding = np.array(embedding.numpy().tolist()[0])

    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='Rex1993',
        host='localhost',
        port='5432'
    )
    cur=conn.cursor()

    register_vector(conn)
    
    # Query to search for movies released in 1988
    query = "SELECT * FROM movie_plots ORDER BY embedding <-> %s LIMIT 5;"

    # Execute the query with the embedding vector
    cur.execute(query, (embedding,))

    # Fetch all results
    results = cur.fetchall()
    
    # Close the cursor and connection
    cur.close()
    conn.close()

    return results
