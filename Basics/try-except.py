# Demonstrate try..except for error handling (division by zero)

try:
    num = int(input("Enter a number: "))
    div = 10 / num
    print(f"10 divided by {num} is {div}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid integer.")

