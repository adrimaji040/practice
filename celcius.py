import sys


try:
    x = int(input("Type  Celsius:"))
    y = (x * 9/5) + 32
except ValueError:
    print("Invalid Input")
    sys.exit(1)

print(f"the celsius {x}, is {y} Fahrenheit")