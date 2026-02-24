import os, json #converts json files into python and vice versa

DATA_FOLDER = "data"

USERS_FILE = "data/users.json"
METERS_FILE ="data/meters.json"
PURCHASES_FILE = "data/purchases.json"

def ensure_data_files():
    #Create the data folder if it does not exist
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

   #create the json files if they do not exist, and start them with []
    file_paths = [USERS_FILE, METERS_FILE, PURCHASES_FILE]

    for file_path in file_paths:
        if not os.path.exists(file_path):
            new_file = open(file_path, "w")
            new_file.write("[]")
            new_file.close()

def read_list(file_path):
   #Make syre files exist
    ensure_data_files()

    #read file text
    file_handle = open(file_path, "r")
    file_text = file_handle.read()
    file_handle.close()

    #convert json text to python list
    return json.loads(file_text)

def write_list(file_path, data_list):
    #Make sure files exist
    ensure_data_files()

    #convert python list to json text
    file_text = json.dumps(data_list)

    #write json text to file
    file_handle = open(file_path, "w")
    file_handle.write(file_text)
    file_handle.close()

def get_next_id(data_list):
    #next id = number of items+1
    return len(data_list) + 1

def load_users():
    return read_list(USERS_FILE)

def save_users(users_list):
    write_list(USERS_FILE, users_list)

def load_meters():
    return read_list(METERS_FILE)

def save_meters(meters_list):
    write_list(METERS_FILE, meters_list)

def load_purchases():
    return read_list(PURCHASES_FILE)

def save_purchases(purchases_list):
    write_list(PURCHASES_FILE, purchases_list)

ensure_data_files()