# Movie Recommendation System 

A movie recommendation system is an advanced algorithm designed to suggest films to users based on their preferences and viewing history. By analyzing user data such as previously watched movies, ratings, and viewing patterns, the system predicts and recommends movies that the user is likely to enjoy. On OTT (Over-The-Top) platforms like Netflix, Amazon Prime, and Disney+, these systems play a crucial role in enhancing user experience by offering personalized content. They use techniques such as collaborative filtering, content-based filtering, and hybrid methods to deliver accurate and tailored movie suggestions, thereby increasing user engagement and satisfaction.mkdir images

![UserInterface](/images/Asset3.jpeg)
![Results](/images/Asset2.jpeg)![Results](/images/Asset.jpeg)


!

 
 ## Why build one more MRS when you can watch a movie in any of the OTT ?
Imagine a movie recommendation site tailored specifically to your unique tastes and feelings. Instead of a cluttered screen filled with endless options, this site understands your preferences and recommends movies based on your current mood, the weather, or even special occasions.

Picture this: It's Saturday night, and you're in the mood for a sci-fi adventure. The next weekend, you crave the thrill of a horror film like "The Conjuring." Or perhaps you have a date night planned and want to surprise your significant other with the perfect romantic movie. For someone who struggles to choose what to watch, having a personalized movie recommendation system (MRS) can be a game-changer.

![Confused](images/Asset.jpg)

This MRS learns from your viewing habits and preferences, suggesting movies that fit your current state of mind. Whether you're looking for a relaxing film on a rainy day or an exciting blockbuster when you're feeling adventurous, this system ensures you always have the perfect movie lined up.

By focusing on how you feel and what you need at the moment, this personalized approach simplifies your movie-watching experience, making it more enjoyable and tailored to your unique tastes. With this site, finding the right movie becomes effortless, allowing you to fully enjoy your downtime without the hassle of endless searching.
### System Design 
![Algorithm](/images/systemdesign.jpg)
 ## System Design Overview

The system is divided into four parts:

1. **Data Collection, Modification, and Storage**: 
   - Gathering data, making necessary modifications, and storing it appropriately for future use.

2. **Frontend with Node.js for Search Operations**: 
   - A Node.js-based frontend interface is developed to facilitate search operations.

3. **Flask-Based Backend for Database Search**: 
   - A backend system built with Flask is responsible for searching the database and providing the top 5 search results.

4. **Frontend for Displaying Movie Posters**: 
   - A frontend interface to display the movie posters of the fetched search results.

## Usage

The packages used are listed in the `requirements.txt` file.

Install the packages with:
```bash
pip install -r requirements.txt
```


## Setting Up PGVector in PostgreSQL

To set up PGVector in PostgreSQL, follow these steps:

### Step 1: Install PostgreSQL

Ensure that PostgreSQL is installed on your system. You can download and install it from the [official PostgreSQL website](https://www.postgresql.org/download/).

### Step 2: Install PGVector Extension

1. **Clone the PGVector repository:**

   ```bash
   git clone https://github.com/pgvector/pgvector.git

    ```
    Installation process can be followed from this  [link](https://github.com/pgvector/)

2.  **Install PGvector in Python:**
    PG vector should be also installed in python else it will keep throwing errors.
    To install PG vector in Python.

    ```bash
     pip install pgvector
      ```
    
3. **Create a Table** 
``` bash
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
```
4. **Connect to database**
```bash
conn = psycopg2.connect(
    dbname='postgres',
    user='username',
    password='password',
    host='localhost',
    port='5432'
)
```
5. **Insert in the table**
```bash
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
    '''
```
### Step 3: Run the app 
```bash
python app.py
```