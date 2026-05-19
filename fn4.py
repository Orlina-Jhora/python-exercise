
value = float(input("Enter temperature value: "))
unit = input("Enter unit (C or F): ") 

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def convert(value, unit):
    if unit == "C":
        return celsius_to_fahrenheit(value)
    elif unit == "F":
        return fahrenheit_to_celsius(value)
    else:
        return "Invalid unit!"

print(f"Converted temperature: {convert(value, unit)}")
