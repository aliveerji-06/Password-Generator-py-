import random
import string
import os

def get_password_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12: score += 1

    if score <= 2: return "Weak 🔴"
    elif score == 3: return "Medium 🟡"
    elif score == 4: return "Strong 🟢"
    else: return "Very Strong 💪"

def generate_password(length, use_upper, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_upper: characters += string.ascii_uppercase
    if use_numbers: characters += string.digits
    if use_symbols: characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_passwords(passwords):
    with open("saved_passwords.txt", "a") as f:
        f.write("\n--- New Batch ---\n")
        for p in passwords:
            f.write(p + "\n")
    print("\n✅ Passwords saved to saved_passwords.txt!")

def view_passwords():
    if not os.path.exists("saved_passwords.txt"):
        print("\n❌ No saved passwords found!")
        return
    print("\n--- Saved Passwords ---")
    with open("saved_passwords.txt", "r") as f:
        print(f.read())

def delete_passwords():
    if not os.path.exists("saved_passwords.txt"):
        print("\n❌ No saved passwords to delete!")
        return
    confirm = input("Are you sure you want to delete all saved passwords? (y/n): ").lower()
    if confirm == 'y':
        os.remove("saved_passwords.txt")
        print("\n✅ All saved passwords deleted!")
    else:
        print("\n❌ Deletion cancelled.")

def main():
    while True:
        print("\n" + "=" * 40)
        print("       🔐 PASSWORD GENERATOR")
        print("=" * 40)
        print("1. Generate Passwords")
        print("2. View Saved Passwords")
        print("3. Delete Saved Passwords")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            length = int(input("\nEnter password length (e.g. 12): "))
            use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            count = int(input("How many passwords to generate? "))

            print("\n--- Your Generated Passwords ---")
            passwords = []
            for i in range(count):
                pwd = generate_password(length, use_upper, use_numbers, use_symbols)
                strength = get_password_strength(pwd)
                print(f"{i+1}. {pwd}  [{strength}]")
                passwords.append(pwd)

            save = input("\nSave passwords to a file? (y/n): ").lower()
            if save == 'y':
                save_passwords(passwords)

        elif choice == '2':
            view_passwords()

        elif choice == '3':
            delete_passwords()

        elif choice == '4':
            print("\nThanks for using Password Generator! Stay safe 🔐")
            break

        else:
            print("\n⚠️ Invalid option, please try again.")

main()