# Practice: convert temperatures between Celsius and Fahrenheit.


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    unit = input("Convert from Celsius or Fahrenheit? [C/F]: ").strip().upper()
    temperature = float(input("Temperature: "))

    if unit == "C":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature:.1f} C = {result:.1f} F")
    elif unit == "F":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature:.1f} F = {result:.1f} C")
    else:
        print("Choose C or F.")


if __name__ == "__main__":
    main()
