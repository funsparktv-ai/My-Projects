import random
import string

def generate_password(length=12, include_digits=True, include_punctuation=True):
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_punctuation:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password (default is 12): "))
            if length <= 0:
                print("Invalid length. Please enter a positive number.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'y' or user_input == 'n':
            return user_input == 'y'
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def main():
    print("Welcome to the Password Generator!")
    length = get_password_length()

    include_digits = get_yes_no_input("Include digits? (y/n): ")
    include_punctuation = get_yes_no_input("Include punctuation? (y/n): ")

    generated_password = generate_password(length, include_digits, include_punctuation)
    print(f"Generated password: {generated_password}")

if __name__ == "__main__":
    main()
