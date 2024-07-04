import tensorflow as tf
import json
import pandas as pd 
import tensorflow_hub as hub


# Read the json file and convert them into embeddings using tensor flow 

file_path = 'movie-plots.json'


model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Function to convert text to embeddings
def text_to_embeddings(text):
    embeddings = model([text])
    return embeddings
# read the json file 
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    #print('Parsed JSON data:', data)

def convert_column_to_embeddings(df, column_name):
    df[column_name + '_embeddings'] = df[column_name].apply(text_to_embeddings)
    return df


df = pd.DataFrame(data)
df['Plot'] = df['Plot'].astype(str)
# Convert the 'plot' column to embeddings
df = convert_column_to_embeddings(df, 'Plot')
df.to_csv('movies_with_embeddings.csv', index=False)
