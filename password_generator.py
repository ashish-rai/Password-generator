import random
import string 

def generate_password(length=10):
    
    #Characters that are included in password
    characters = string.ascii_letters + string.digits + string.punctuation

    #Generates password using random choices  from the characters
    password = ''.join(random.choice(characters) for i in range (length))

    return password

def save_password(password):

    #saves the password as txt file
    file_name = input("Save as: ") .strip() + ".txt"
    with open(file_name,'w') as file:
        file.write(password)
    print(f"Password saved as {file_name}")


#Input validation
while True:
    try:
        print("\n***Welcome to Password Generator!***")
        #Get user input for password length.
        user_input = input("\nEnter the length of password you want (or PRESS ENTER to AUTO GENERATE):")

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
            print("Number must be greater than 0")

        else:
            break #Exits the loop if the valid number is entered

    except ValueError:
        #Catch the invalid input and display the prompt agaain
        print("Invalid input!! Enter valid number")

#Generate password after getting valid input
password = generate_password(length)
print(f"Password generated: {password}")

#Ask user to save the password or not
save_pass = input("Do you want to save the password? (y/n):")
if save_pass == 'y':
    save_password(password)

else:
    print("Password not saved")



