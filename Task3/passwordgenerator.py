import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Define character sets
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    generated_password = generate_password(length, use_digits, use_special_chars)
    print(f"Generated Password: {generated_password}")
