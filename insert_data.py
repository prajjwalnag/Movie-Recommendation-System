import pandas as pd
import psycopg2
import tensorflow as tf
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector
import numpy as np


# Read the CSV file into a DataFrame
df = pd.read_csv('movie_plots.csv')


# Check for the required columns
required_columns = ['Title', 'Director', 'Cast', 'Genre', 'Plot', 'Release Year', 'Wiki Page', 'Embeddings']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise KeyError(f"The following required columns are missing from the DataFrame: {missing_columns}")
print("Hakuna Matata")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='Rex1993',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS movie_plots")
# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS movie_plots (
    title VARCHAR,
    director VARCHAR,
    "cast" VARCHAR,
    genre VARCHAR,
    plot TEXT,
    "year" SMALLINT,
    wiki VARCHAR,
    embedding vector(512)
);
''')
conn.commit()
print("Hakuna Matata again")

# Register the vector type
register_vector(conn)

for _, row in df.iloc[:-1].iterrows():
    # Convert tensor to list
    embedding_list = eval(row['Embeddings'])[0]
    embedding_list=np.array(embedding_list)
    print(embedding_list)
    # print(row['Title'],
    #     row['Director'],
    #     row['Cast'],
    #     row['Genre'],
    #     row['Plot'],
    #     row['Release Year'],
    #     row['Wiki Page'],
    #     vector)
    
    
    cursor.execute('''
    INSERT INTO movie_plots (title, director, "cast", genre, plot, "year", wiki, embedding)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                   
    ''', (
        row['Title'],
        row['Director'],
        row['Cast'],
        row['Genre'],
        row['Plot'],
        row['Release Year'],
        row['Wiki Page'],
        embedding_list,
    ))
# Commit the transaction to save changes
    conn.commit()
    print("*")
print("Hakuna Matata 2X again")

# Close the connection
cursor.close()
conn.close()