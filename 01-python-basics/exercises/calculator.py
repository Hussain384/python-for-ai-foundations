# Practice: build a calculator with functions, conditions, and input.


def calculate(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ValueError("Cannot divide by zero")
        return first / second
    raise ValueError("Unknown operator")


def main():
    first = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ").strip()
    second = float(input("Second number: "))

    try:
        result = calculate(first, operator, second)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
