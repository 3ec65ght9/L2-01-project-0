# Function goes here
def int_check(question):
    """Check users enter an integer between two values"""

    error = f"Oops - please enter an integer."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))
            return response

        except ValueError:
            print(error)


# Main Routine goes here

# Loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = input("Name: ")  # replace with call to 'not blank' function!

    # Ask for their age check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
