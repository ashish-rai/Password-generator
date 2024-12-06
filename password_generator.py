import random
import string 

def generate_password(length=10):
    
    #Characters that are included in password
    characters = string.ascii_letters + string.digits + string.punctuation

    #Generates password using random choices  from the characters
    password = ''.join(random.choice(characters) for i in range (length))

    return password

#Input validation
while True:
    try:

        #Get user input for password length.
        user_input = input("\n******\nEnter the length of password you want (or PRESS ENTER to AUTO GENERATE):\n******\n")

        #If user press Enter (It auto generates the password of default length=10)
        if user_input == "":
            length = 10
            print("Auto-generating password......") 
            break
        else:
            #If user puts the value convert it into integer.
            length = int(user_input)

        #Check if the number is positive
        if length <= 0:
            print("Please enter positive number")

        else:
            break #Exits the loop if the valid number is entered

    except ValueError:
        #Catch the invalid input and display the prompt agaain
        print("Invalid input!! Enter valid number")

#Generate password after getting valid input
password = generate_password(length)
print(f"Password generated: {password}")


