import random
import string

def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' number of characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                print("Please enter a positive password length.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for password length.")

    password = generate_password(password_length)
    print(f"Generated Password: {password}")


