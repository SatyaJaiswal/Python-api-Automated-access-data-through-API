import json

def register_admin(username, password):
    admin_credentials = {}
    
    try:
        # Load existing credentials from the JSON file
        with open('admin_credentials.json', 'r') as file:
            admin_credentials = json.load(file)
    except FileNotFoundError:
        # If the JSON file doesn't exist, create an empty dictionary
        pass

    if username in admin_credentials:
        print("Username already exists. Please choose a different username.")
    else:
        # Add the new admin username and password to the dictionary
        admin_credentials[username] = password

        # Save the updated credentials to the JSON file
        with open('admin_credentials.json', 'w') as file:
            json.dump(admin_credentials, file, indent=4)
        print("Admin registration successful.")

if __name__ == '__main__':
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
    register_admin(admin_username, admin_password)
