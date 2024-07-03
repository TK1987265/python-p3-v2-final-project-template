# lib/helpers.py
# from models import SessionLocal
from models import  Session, Wrestler, Team

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def add_wrestler():
    print("Adding a new wrestler...")
    name = input("Enter the wrestler's name: ")
    weight_class = input("Enter the wrestler's weight class: ")
    team_id = input("Enter the wrestler's team ID (must be an existing team): ")


    if not name or not weight_class or not team_id.isdigit():
        print("Invalid input, please try again.")
        return

    # Add the wrestler to the database
    session = Session()
    new_wrestler = Wrestler(name=name, weight_class=weight_class, team_id=int(team_id))
    session.add(new_wrestler)
    try:
        session.commit()
        print(f"Wrestler {name} added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()



def list_wrestlers():
    print("Listing all wrestlers...")
    session = Session()
    wrestlers = session.query(Wrestler).all()
    if wrestlers:
        for wrestler in wrestlers:
            print(f"ID: {wrestler.id}, Name: {wrestler.name}, Weight Class: {wrestler.weight_class}, Team: {wrestler.team.name if wrestler.team else 'No Team'}")
    else:
        print("No wrestlers found.")


def add_team():
    print("Adding a new team...")
    team_name = input("Enter the team's name: ")
    session = Session()
    if session.query(Team).filter(Team.name == team_name).first():
        print("Team already exists.")
    else:
        new_team = Team(name=team_name)
        session.add(new_team)
        session.commit()
        print(f"Team '{team_name}' added successfully.")

# Function to list all teams
def list_teams():
    print("Listing all teams...")
    session = Session()
    teams = session.query(Team).all()
    if teams:
        for team in teams:
            print(f"ID: {team.id}, Name: {team.name}")
    else:
        print("No teams found.")


