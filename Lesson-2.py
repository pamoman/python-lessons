# Pamoman Python - Lesson 2

# While Loop with input

while True:
    try:
        amount = input("Type an amount: ")

        # Convert the user amount into a decimal number
        a = float(amount)

        # Round a to 2 decimal points using string formatting
        b = "{:.2f}".format(a)

        # Concatenate b with kr
        c = b + "kr"

        # Finished: Now we print the final result
        print(c)

        # If you got here then everything went well, let's break the loop
        break
    except:
        # An error occured so print an error message
        print("Error: No strings allowed! \nTry again.")
        # then continue with a new loop