import hashlib
from time import sleep
from decorators import log
from storage import load_users, save_users, get_next_id
from models import User


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    

def find_user_by_username(user_list, username):
    for user in user_list:
        if user["username"] == username:
            return user
    return None


def username_is_valid(username):
    if username == "":
        print("Username cannot be empty.")
        return False 
    if len(username) < 5:
        print("Username must be at least 5 characters.")
        return False
    if len(username) > 20:
        print("Username must be at most 20 characters.")
        return False
    return True


def password_is_valid(password):
    if password == "":
        print("Password cannot be empty.")
        return False
    if len(password) < 5:
        print("Password must be at least 5 characters.")
        return False
    if " " in password:
        print("Password cannot contain spaces.")
        return False
    
    has_letter = False
    has_number = False
    for ch in password:
        if ch.isalpha():
            has_letter = True
        if ch.isdigit():
            has_number = True

    if has_letter == False:
        print("Password must contain at least 1 letter.")
        return False
    
    if has_number == False:
        print("Password must contain at least 1 number.")
        return False
    return True


@log
def register():
    users_list = load_users()

    print("\n---- REGISTER ----")
    print("Type 0 to cancel.")

    while True:
        username = input("Create username: ").strip()

        if username == "0":
            print("Cancelled.")
            sleep(1)
            return None

        if not username_is_valid(username):
            sleep(1)
            continue
        
        if find_user_by_username(users_list, username) is not None:
            print("Username already exists.")
            sleep(1)
            continue

        break
    
    print("\nPassword rules:")
    print("- At least 5 characters")
    print("- Must contain at least 1 letter")
    print("- Must contain at least 1 number")
    print("- No spaces")
    print("Type 0 to cancel.")
    while True:
        password = input("Create a password: ").strip()

        if password == "0":
            print("Cancelled.")
            sleep(1)
            return None

        if not password_is_valid(password):
            sleep(1)
            continue

        confirm = input("Confirm password: ").strip()

        if confirm == "0":
            print("Cancelled.")
            sleep(1)
            return None

        if confirm != password:
            print("Passwords do not match.")
            sleep(1)
            continue

        break
    

    new_id = get_next_id(users_list)

    user_object = User(
        user_id=new_id,
        username=username,
        password_hash=hash_password(password),
        is_locked=False
    )

    users_list.append(user_object.user_to_dict())
    save_users(users_list)

    print("Account has been created.")
    sleep(1)
    return user_object.user_to_dict()


@log
def login():
    users_list = load_users()

    print("\n---- LOGIN ----")
    print("Type 0 to cancel.")
    
    user = None
    user_tries = 0

    while user is None:
        username = input("Username: ").strip()

        if username == "0":
            print("Cancelled.")
            sleep(1)
            return None
        
        user = find_user_by_username(users_list, username)

        if user is None:
            user_tries = user_tries + 1
            wait_seconds = 1 + (user_tries * 2)
            print("User not found.")
            print(f"Please wait {wait_seconds} seconds...")
            sleep(wait_seconds)
    

    if user.get("is_locked") == True:
        print("Account locked. Please contact support.")
        sleep(2)
        return None
    

    password_tries = 0
    while password_tries < 3:
        password = input("Password: ").strip()

        if password == "0":
            print("Cancelled.")
            sleep(1)
            return None

        if hash_password(password) == user["password_hash"]:
            print("Login successful.")
            sleep(1)
            return user
        
        password_tries = password_tries + 1
        wait_seconds = 1 + (password_tries * 2)
        print(f"Wrong password {3 - password_tries} tries remaining.")
        print(f"Please wait {wait_seconds} seconds...")
        sleep(wait_seconds)

    user["is_locked"] = True
    save_users(users_list)

    print("Too many tries. Account has been locked.")
    sleep(2)
    return None