import sqlite3

def create_tables():
    connection = sqlite3.connect('wrestling.db')
    cursor = connection.cursor()

    # Create the 'teams' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE
    )
    ''')

    # Create the 'wrestlers' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wrestlers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        weight_class TEXT,
        team_id INTEGER,
        FOREIGN KEY (team_id) REFERENCES teams(id)
    )
    ''')

    connection.commit()
    connection.close()

create_tables()

def get_db_connection():
    connection = sqlite3.connect('wrestling.db')
    connection.row_factory = sqlite3.Row
    return connection