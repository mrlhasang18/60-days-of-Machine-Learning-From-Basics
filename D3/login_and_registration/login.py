# Creating login file
file = open("login.txt", 'w')
file.write("Username and passwords\n")
file.close()

#to load users
def load_users():
    users = {}
    with open("login.txt", 'r') as file:
        lines = file.readlines()
        for i in lines[1:]:  # Skip the first line (header)
            username, password = i.strip().split()
            users[username] = password
    return users


def login_register():
    print(" -------- Welcome to login and registration system --------")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        login()
    elif choice == 2:
        register()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice")
        login_register()

def login():
    users = load_users()
    print("------- Welcome to login page --------")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful")
    else:
        print("Invalid username or password")
        login_register()

def register():
    users = load_users()
    print("----------- Welcome to registration page ---------")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users:
        print("Username already exists. Please try again.")
        login_register()
    else:
        with open("login.txt", 'a') as file:
            file.write(username + " " + password + "\n")
        print("Registration successful")
        print("Automatically logging in...")
        login()

login_register()
