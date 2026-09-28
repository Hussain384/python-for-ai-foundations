# Practice: validate a password using conditions.


def check_password(password):
    checks = {
        "at least 8 characters": len(password) >= 8,
        "an uppercase letter": any(character.isupper() for character in password),
        "a lowercase letter": any(character.islower() for character in password),
        "a digit": any(character.isdigit() for character in password),
    }
    return checks


def main():
    password = input("Enter a password to check: ")
    checks = check_password(password)
    failed_checks = [name for name, passed in checks.items() if not passed]

    if not failed_checks:
        print("Password meets all basic requirements.")
    else:
        print("Missing: " + ", ".join(failed_checks))


if __name__ == "__main__":
    main()
