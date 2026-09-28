# Practice: inspect whether a number is positive, negative, zero, even, or odd.


def describe_number(number):
    if number == 0:
        sign = "zero"
    elif number > 0:
        sign = "positive"
    else:
        sign = "negative"

    parity = "even" if number % 2 == 0 else "odd"
    return f"{number} is {sign} and {parity}."


def main():
    number = int(input("Enter an integer: "))
    print(describe_number(number))


if __name__ == "__main__":
    main()
