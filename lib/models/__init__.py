import sqlite3


def setup_application():
    print("Setting up the database...")
    create_tables()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_application()

# from team_model import Wrestler, Team, SessionLocal
CONN = sqlite3.connect('wrestling.db')
CURSOR = CONN.cursor()





def create_tables():
    print("Creating tables...")  # Debugging output
    try:
        connection = sqlite3.connect('wrestling.db')
        cursor = connection.cursor()
        print("Connected to SQLite")

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        );
        ''')
        print("Teams table created")

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS wrestlers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            weight_class TEXT NOT NULL,
            team_id INTEGER,
            FOREIGN KEY (team_id) REFERENCES teams(id)
        );
        ''')
        print("Wrestlers table created")

        connection.commit()
        print("Commit successful")

    except sqlite3.Error as error:
        print("Error while creating tables", error)
    finally:
        if (connection):
            connection.close()
            print("SQLite connection is closed")
