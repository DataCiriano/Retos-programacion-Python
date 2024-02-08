
from cryptography.fernet import Fernet
import os

# Function to create a cryptography key
def generate_key():
    key = Fernet.generate_key()
    
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Uncomment the following line to generate the key if it hasn't been generated yet
#generate_key()

# Loading function for the created cryptography key
def load_key():
    try:
        with open("key.key", "rb") as file:
            key = file.read()
        return key
    except FileNotFoundError:
        print("Key file not found. Please run the 'generate_key()' function to create a key.")
        exit()

# Function to create or update the master password
def create_master_password(fernet):
    # Ask the user to set or update the master password
    master_password = input("Set or update the master password: ")
    
    # Encrypt and store the master password
    encrypted_master_password = fernet.encrypt(master_password.encode())
    with open("master_password.txt", "wb") as master_file:
        master_file.write(encrypted_master_password)

# Function to check the master password
def check_master_password(fernet):
    # Ask the user to enter the master password
    entered_master_password = input("Enter the master password: ")
        
    # Read and decrypt the stored master password
    try:
        with open("master_password.txt", "rb") as master_file:
            encrypted_master_password = master_file.read()
        decrypted_master_password = fernet.decrypt(encrypted_master_password).decode()
        return entered_master_password == decrypted_master_password
    except ValueError:
        return False

# Exceptions management
try:
    key = load_key()
except FileNotFoundError:
    print("Key file not found. Generating a new key.")
    generate_key()
    key = load_key()

# Initialize Fernet object globally
fernet = Fernet(key)

# Check if the master password has been set
if not os.path.exists("master_password.txt"):
    create_master_password(fernet)
else:
    while not check_master_password(fernet):
        print("Incorrect master password. Please try again.")
    print("Master password is correct.")

# Function for 'view' mode
def view():
    with open('password.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, psw, information = data.split("|")
            decrypted_password = fernet.decrypt(psw.encode()).decode()
            print("User:", user, "|", "Password:", decrypted_password, "|", "Information:", information)

# Function for 'add' mode
def add():
    name = input("User: ")
    password = input("Password: ")
    info = input("Information: ")
    
    with open('password.txt', 'a') as file:
        encrypted_password = fernet.encrypt(password.encode()).decode()
        file.write(name + "|" + encrypted_password + "|" + info + "\n")

while True:
    mode = input("Type (view) to see your stored passwords, (add) to save a new one, or (q) to quit: ").lower()
    
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
        continue