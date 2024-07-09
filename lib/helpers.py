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


# add a new team
def add_team(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO teams (name) VALUES (?)', (name,))
        conn.commit()
        print(f"Team '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Team '{name}' already exists.")
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

# get all wrestlers
def get_all_wrestlers():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Join the wrestlers table with the teams table to get team names
        cursor.execute('''
            SELECT w.id, w.name, w.weight_class, w.team_id, t.name as team_name 
            FROM wrestlers w
            JOIN teams t ON w.team_id = t.id
        ''')
        wrestlers = cursor.fetchall()
        
        # Check if any wrestlers were found
        if wrestlers:
            print("List of all wrestlers:")
            for wrestler in wrestlers:
                print(f"ID: {wrestler['id']}, Name: {wrestler['name']}, Weight Class: {wrestler['weight_class']}, Team ID: {wrestler['team_id']}, Team Name: {wrestler['team_name']}")
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

# print all teams
def print_teams():
    teams = get_teams()
    for team in teams:
        print(f"Team ID: {team['id']}, Name: {team['name']}")


# delete wrestler
def delete_wrestler(wrestler_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM wrestlers WHERE id = ?', (wrestler_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("No wrestler found with the specified ID.")
        else:
            print("Wrestler deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def delete_team(team_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
       
        cursor.execute('SELECT * FROM wrestlers WHERE team_id = ?', (team_id,))
        if cursor.fetchone() is not None:
            print("Cannot delete team with wrestlers assigned to it.")
            return

        cursor.execute('DELETE FROM teams WHERE id = ?', (team_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("No team found with the specified ID.")
        else:
            print("Team deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()



def find_wrestler_by_name(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Join with the teams table to get the team name
        cursor.execute('''
        SELECT w.id, w.name, w.weight_class, t.name as team_name
        FROM wrestlers w
        LEFT JOIN teams t ON w.team_id = t.id
        WHERE w.name LIKE ?
        ''', ('%' + name + '%',))
        wrestlers = cursor.fetchall()
        if wrestlers:
            print("Found wrestlers:")
            for wrestler in wrestlers:
                print(f"ID: {wrestler['id']}, Name: {wrestler['name']}, Weight Class: {wrestler['weight_class']}, Team Name: {wrestler['team_name']}")
        else:
            print("No wrestlers found with the given name.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def find_team_by_name(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM teams WHERE name LIKE ?', ('%' + name + '%',))
        teams = cursor.fetchall()
        if teams:
            print("Found teams:")
            for team in teams:
                print(f"ID: {team['id']}, Name: {team['name']}")
        else:
            print("No teams found with the given name.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

