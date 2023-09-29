import random as r
import string as st
import csv

def generate_password(length=10):
    characters = st.ascii_letters + st.digits + st.punctuation
    return ''.join(r.choice(characters) for _ in range(length))

def save_to_csv(name, password):
    with open('passwords.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, password])
    print(f"Password for '{name}' saved to 'passwords.csv'.")

if __name__ == "__main__":
    while True:
        print("\nPassword Manager Menu:")
        print("1. Generate Password and Save to CSV")
        print("2. Quit")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            name = input("Enter your name: ")
            length_input = input("Enter the desired password length: ")
            password_length = int(length_input) if length_input.strip() else 12
            generated_password = generate_password(password_length)
            save_to_csv(name, generated_password)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("\n \nBye Bye Dosto!\n \n")
