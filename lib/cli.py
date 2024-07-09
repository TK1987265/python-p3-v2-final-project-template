from helpers import (
    exit_program,
    add_wrestler,
    add_team,
    print_teams,
    get_all_wrestlers,
    delete_wrestler,
    delete_team,
    find_wrestler_by_name,
    find_team_by_name
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
           add_wrestler()
        elif choice == "2":
            get_all_wrestlers()
        elif choice == "3":
            team_name = input("Enter team's name: ")
            add_team(team_name)
        elif choice == "4":
            print_teams()
        elif choice == "5":
            wrestler_id = input("Enter wrestler ID to delete: ")
            delete_wrestler(wrestler_id)
        elif choice == "6":
            team_id = input("Enter team ID to delete: ")
            delete_team(team_id)
        elif choice == "7":
            wrestler_name = input("Enter wrestler's name to search: ")
            find_wrestler_by_name(wrestler_name)
        elif choice == "8":
            team_name = input("Enter team's name to search: ")
            find_team_by_name(team_name)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new wrestler")
    print("2. List all wrestlers")
    print("3. Add a new team")
    print("4. List all teams")
    print("5. Delete a wrestler")
    print("6. Delete a team")
    print("7. Find a wrestler by name")
    print("8. Find a team by name")

if __name__ == "__main__":
    main()
