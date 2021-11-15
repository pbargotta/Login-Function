# creates a login system that can create new accounts and store them in an external text file and allow for a user
# to login into an existing account
def login_system():
    LOGIN_FILE = "Logins.txt"

    def getlogins():
        # opens text file as read-only and returns each line of the file in a list then closes the file to save memory
        logins_file = open(LOGIN_FILE, "r")
        all_logins = logins_file.readlines()
        logins_file.close()

        logins = {}
        # iterates through all of the lines in the files and splits each line of the file into its username and password
        # component and then saves them into the 'logins' dictionary and returns it
        for line in range(len(all_logins)):
            login_line = all_logins[line]
            login_components = login_line.strip().split(",")
            username_component = login_components[0]
            password_component = login_components[1]
            logins[username_component] = password_component
        return logins

    # create function to ask the user to login to an account
    def login():
        accounts = getlogins()
        logged_in = False

        while not logged_in:
            username_attempt = input("Enter your username.\n")
            password_attempt = input("Enter your password.\n")

            # iterates through all current accounts and checks if the username attempt is valid and if it is
            # then it checks if the password attempt matches the username,
            # if either component is invalid, it gives an error and allows the user to retry
            for username in accounts:
                if username_attempt == username:
                    if password_attempt == accounts[username]:
                        print(f"Welcome {username}!\n")
                        logged_in = True
            if not logged_in:
                print("Invalid username and/or password. Please try again.\n")

    # creates a function that can create new accounts and store them in an external text file
    def create_account():
        accounts = getlogins()
        unique_username = False
        new_username = input("What would you like to be your username?\n")

        # iterates through all existing usernames and checks if the new username is unique, if is not,
        # it will continuously run until a unique name is entered
        while not unique_username:
            checked_accounts = 0
            for username in accounts:
                if new_username == username:
                    print("That username is already taken. Please choose something else.\n")
                    new_username = input("What would you like to be your username?\n")
                    break
                checked_accounts += 1
            if checked_accounts == len(accounts):
                unique_username = True

        new_password = input("What would you like to be your password?\n")
        print(f"Welcome {new_username}!\n")

        # opens the 'logins' file to append in the new username and password together and then will close the file
        logins_file = open(LOGIN_FILE, "a")
        logins_file.write(f"{new_username},{new_password}\n")
        logins_file.close()

    def main_system():
        user_input = input("Would you like to login to an existing account or "
                           "would you like to create a new account? ('L' / 'C')\n").upper()

        while user_input != "L" and user_input != "C":
            user_input = input("Please choose to login to an existing account or create a new one with either the input"
                               " 'L' or 'C'\n").upper()

        if user_input == "L":
            login()
        elif user_input == "C":
            create_account()

    main_system()
