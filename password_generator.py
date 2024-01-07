#Developed by: Ratshili Masala Gift
#Task Name: Password Generator
#Company: CodSoft Internship
#Status: Completed

import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level. Please choose 'low', 'medium', or 'high'."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the password length: "))
        complexity = input("Enter the complexity level (low/medium/high): ").lower()

        password = generate_password(length, complexity)
        print("Generated Password: " + password)

    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
