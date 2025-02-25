def not_blank(questions):
    """Check that a user response is not blanks"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


# main routine starts here
who = not_blank("Please enter your name:Arem ")
print(f"Hello {who}")
