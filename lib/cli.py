from helpers import (
    exit_program,
    helper_1,
    add_team,
    add_wrestler,
    print_teams,
    get_all_wrestlers
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_wrestler()
        elif choice == "3":
            add_team()
        elif choice == "2":
            get_all_wrestlers()
        elif choice == "4":
            print_teams()
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
