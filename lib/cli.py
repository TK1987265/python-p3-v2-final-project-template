from helpers import (
    exit_program,
    add_wrestler,
    list_wrestlers,
    add_team,
    list_teams
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
            list_wrestlers()
        elif choice == "3":
            add_team()
        elif choice == "4":
            list_teams()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new wrestler")
    print("2. List all wrestlers")
    print("3. Add a new team")
    print("4. List all teams")

if __name__ == "__main__":
    main()
