# A simple program to convert a user input into an integer
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"You entered {number}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
