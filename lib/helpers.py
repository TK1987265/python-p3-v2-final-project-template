import sqlite3


# Database connection 
def get_db_connection():
    conn = sqlite3.connect('wrestling.db')
    conn.row_factory = sqlite3.Row
    return conn

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()


# Add a new team to the database
def add_team():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Prompt for the team name within the function
        team_name = input("Enter the name of the new team: ")
        cursor.execute('INSERT INTO teams (name) VALUES (?)', (team_name,))
        conn.commit()
        print(f"Team '{team_name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Team '{team_name}' already exists.")
    finally:
        conn.close()

# Add a new wrestler to a specific team
def add_wrestler():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # User input for wrestler details
        name = input("Enter the wrestler's name: ")
        weight_class = input("Enter the wrestler's weight class: ")
        team_id = input("Enter the team ID for the wrestler: ")


        team_id = int(team_id)
        cursor.execute('''
        INSERT INTO wrestlers (name, weight_class, team_id) VALUES (?, ?, ?)
        ''', (name, weight_class, team_id))
        conn.commit()
        print(f"Wrestler '{name}' added successfully.")
    except ValueError:
        print("Invalid input: Team ID must be a number.")
    except sqlite3.IntegrityError:
        print(f"Error adding wrestler '{name}'. Make sure the team exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()


# Get all teams
def get_teams():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM teams')
        teams = cursor.fetchall()
        return teams
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def get_all_wrestlers():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
      
        cursor.execute('SELECT * FROM wrestlers')
        wrestlers = cursor.fetchall()
        
       
        if wrestlers:
            print("List of all wrestlers:")
            for wrestler in wrestlers:
                print(f"ID: {wrestler['id']}, Name: {wrestler['name']}, Weight Class: {wrestler['weight_class']}, Team ID: {wrestler['team_id']}")
        else:
            print("No wrestlers found in the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Get all wrestlers in a team
def get_wrestlers_by_team(team_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM wrestlers WHERE team_id = ?
    ''', (team_id,))
    wrestlers = cursor.fetchall()
    conn.close()
    return wrestlers

# Example utility to print all teams
def print_teams():
    teams = get_teams()
    for team in teams:
        print(f"Team ID: {team['id']}, Name: {team['name']}")
