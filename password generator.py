import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter desired password length (default is 12): "))
        if password_length <= 0:
            print("Invalid length. Using default length of 12.")
            password_length = 12
    except ValueError:
        print("Invalid input. Using default length of 12.")
        password_length = 12

    generated_password = generate_password(password_length)
    print(f"Your magical password: {generated_password}")

if __name__ == "__main__":
    main()