import hashlib
from time import sleep
from decorators import log
from storage import load_users, save_users, get_next_id
from models import User

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

    
def find_user_by_username(user_list, username):
    for  user in user_list:
        if user["username"]== username:
            return user 
    return None

def username_is_valid(username):
    if username == "":
        return False 
    if len(username) < 5:
        return False
    return True


def password_is_valid(password):
    if password =="":
        return False
    if len(password) < 4:
        return False
    return True
@log
def register():
    users_list = load_users()
    print("REGISTER")
    username = input("Create username: ").strip()

    if not username_is_valid(username):
        print("Username must be at least 5 characters.")
        return None
    
    if find_user_by_username(users_list, username):
        print("Username already exist.")
        return None
    
    password = input("Create a password: ").strip()

    if not password_is_valid(password):
        print("Password must be at least 4 character")
        return None
    
    new_id = get_next_id(users_list)

    user_object = User(
        user_id = new_id,
        username = username,
        password_hash=hash_password(password),
        is_locked= False

    )
    users_list.append(user_object.user_to_dict())
    save_users(users_list)
    print("Account has been created.")
    return user_object.user_to_dict()


def login():

    users_list = load_users()
    print("----LOGIN----")
    username = input("username: ").strip()

    user = find_user_by_username(users_list, username)
    if user is None:
        print("User not found.") 
        return None
    
    if user.get("is_locked ") == True:
        print("Account locked.")
        return None
    tries = 0
    while tries < 3:
        password = input("Paassword: ").strip()

        if hash_password(password) == user["password_hash"]:
            print("Login successful.")
            return User
        
        tries = tries + 1
        print(f"Wrong password {3 -tries} tries remaining.")
    user["is_locked"] = True
    save_users(users_list)

    print("Too many tries . Account has been locked")