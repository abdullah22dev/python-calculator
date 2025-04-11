import math
import statistics

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def mean(numbers):
    return statistics.mean(numbers)

def median(numbers):
    return statistics.median(numbers)

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Cannot take square root of a negative number."

def main():
    while True:
        print("\n--- Basic Python Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Mean")
        print("6. Median")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))

        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", subtract(a, b))

        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", multiply(a, b))

        elif choice == '4':
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            print("Result:", divide(a, b))

        elif choice == '5':
            nums = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Mean:", mean(nums))

        elif choice == '6':
            nums = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Median:", median(nums))

        elif choice == '7':
            x = float(input("Enter a number: "))
            print("Square Root:", square_root(x))

        elif choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid input. Please choose a number between 1 and 8.")

if __name__ == "__main__":
    main()
