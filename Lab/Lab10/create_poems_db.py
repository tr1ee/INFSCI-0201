
import sqlite3

def create_and_populate_db():

    conn = sqlite3.connect('poems.db')
    cursor = conn.cursor()

    # Create the poems table
    cursor.execute("""CREATE TABLE poems (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        text TEXT
    );
    """)

    # Insert poem data into the poems table
    poems_data = [
        ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
        ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
        ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high oer vales and hills...'),
        ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summers day? Thou art more lovely and more temperate...'),
        ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
    ]

    # Execute insert statement for each poem
    cursor.executemany('INSERT INTO poems (title, author, text) VALUES (?, ?, ?)', poems_data)
    conn.commit()  # Commit changes to the database

    # Close connection
    conn.close()

if __name__ == '__main__':
    create_and_populate_db()
