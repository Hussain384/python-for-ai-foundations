# Practice: build a menu-driven program with a loop.


def show_menu():
    print("\n1. Say hello")
    print("2. Show a number")
    print("3. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Hello, Python!")
        elif choice == "2":
            print("Your practice number is 42.")
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
