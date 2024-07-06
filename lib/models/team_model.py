import sqlite3

def get_db_connection():
    connection = sqlite3.connect('wrestling.db')
    connection.row_factory = sqlite3.Row
    return connection
class Team:
    def __init__(self, name, _id=None):
        self.id = _id
        self.name = name

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO teams (name) VALUES (?)', (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE teams SET name = ? WHERE id = ?', (self.name, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def add_team(name):
        # Check if the team already exists
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM teams WHERE name = ?', (name,))
        row = cursor.fetchone()
        if row:
            return Team(name=name, _id=row[0])
        else:
            new_team = Team(name)
            new_team.save()
            return new_team

class Wrestler:
    def __init__(self, name, weight_class, team_id, _id=None):
        self.id = _id
        self.name = name
        self.weight_class = weight_class
        self.team_id = team_id

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO wrestlers (name, weight_class, team_id) VALUES (?, ?, ?)', 
                        (self.name, self.weight_class, self.team_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE wrestlers SET name = ?, weight_class = ?, team_id = ? WHERE id = ?', 
                        (self.name, self.weight_class, self.team_id, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def add_wrestler(name, weight_class, team_id):
        # Create and save a new wrestler
        new_wrestler = Wrestler(name, weight_class, team_id)
        new_wrestler.save()
        return new_wrestler

# Example usage
team = Team.add_team("Red Warriors")
wrestler = Wrestler.add_wrestler("John Doe", "Heavyweight", team.id)
