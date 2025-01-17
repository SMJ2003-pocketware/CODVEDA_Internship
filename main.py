#Basic File Encryption/Decryption
#Name:Soham Majumder

#demo file: C:\Users\soham\OneDrive\Desktop\Soham Majumder\internships\Codveda Technologies\INTERNSHIP_TASKS\Level-3 (Advanced)\file encrypt and decrypt\demo.txt
#location for encrypted file: C:\Users\soham\OneDrive\Desktop\Soham Majumder\internships\Codveda Technologies\INTERNSHIP_TASKS\Level-3 (Advanced)\file encrypt and decrypt\demo_encrypted.txt


#importing the required libraries and the dependencies
from cryptography.fernet import Fernet
import os

#creating the functions required for the project
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'key.key'.")

def load_key():
    if not os.path.exists("key.key"):
        raise FileNotFoundError("Key file not found. Please generate a key first.")
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(input_file, output_file):
    key = load_key()
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    print(f"The encrypted file has been created at: {output_file}")

def decrypt_file(input_file, output_file):
    key = load_key()
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print(f"The encrypted file has been decrypted and saved at: {output_file}")

def main():
    print("Basic File Encryption/Decryption Tool")
    print("1. Generate Encryption Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")
    while True:
        choice = input("Enter your desired choice:")
        if choice == "1":
            generate_key()
        elif choice == "2":
            input_file = input("Enter the path of the file to encrypt: ")
            output_file = input("Enter the path for the encrypted file: ")
            encrypt_file(input_file, output_file)
        elif choice == "3":
            input_file = input("Enter the path of the file to decrypt: ")
            output_file = input("Enter the path for the decrypted file: ")
            decrypt_file(input_file, output_file)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
