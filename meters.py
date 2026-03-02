from storage import load_meters, save_meters, get_next_id
from models import Meter
from time import sleep

def add_meter(current_user):
    meters_list = load_meters()
    
    print("\n---- Add Meter ----")
    print("Type 0 to cancel.")
    while True:
        meter_number = input("Enter meter number: ").strip()
        if meter_number == "0":
            print("Cancelled.")
            sleep(1)
            return None
        
        if meter_number == "":
            print("Meter number cannot be empty.")
            sleep(1)
            continue
        
        if not meter_number.isdigit():
            print("Meter number must contain digits only.")
            sleep(1)
            continue
        
        if len(meter_number) != 11 and len(meter_number) != 13:
            print("Meter number must be 11 or 13 digits.")
            sleep(1)
            continue
        
        duplicate_found = False
        for meter in meters_list:
            if meter["user_id"] == current_user["id"] and meter["meter_number"] == meter_number:
                duplicate_found = True
                break
        if duplicate_found:
            print("That meter is already saved on your account.")
            sleep(1)
            continue
        break

    while True:    
        alias = input("Enter alias (example: Home): ").strip()
        if alias == "0":
            print("Cancelled.")
            sleep(1)
            return None
        
        if alias == "":
            print("Alias cannot be empty.")
            sleep(1)
            continue
        break
    
    new_id = get_next_id(meters_list)
    meter_object = Meter(
        meter_id = new_id,
        user_id = current_user["id"],
        meter_number = meter_number,
        alias= alias
    )
    
    meters_list.append(meter_object.meter_to_dict())
    save_meters(meters_list)
    print("Meter has been created.")
    sleep(1)
    return meter_object.meter_to_dict()
     
def list_meters(current_user):
    
    meters_list = load_meters()
    
    users_meters = []
 
    
    """
        for meter in meters_list
        means go through the meters one by one using a new variable created called 'meter'
        Imagine meters_list is
        meters_list = [
        {
            "meter_number": 1111111111111111
            "alias": "Home"
        }, 
        {
            "meter_number": 1111111111111112
            "alias": "Shop"
        }, {}
        ]
        for meter in meters_list:
        print(meter)
        meter -> (1) {
            "meter_number": 1111111111111111
            "alias": "Home"
        }
        meter -> (2) {
            "meter_number": 1111111111111112
            "alias": "Shop"
        }
        The meter is a temporary variable that holds the current meter during the loop
        """
    
    for meter in meters_list:
        if meter ["user_id"] == current_user["id"]:
            users_meters.append(meter)
    
    if len(users_meters) == 0:
        print("No meter found.")
        sleep(1)
        return []
    
    print("\n---- Your Meters ----")
    for i in range(len(users_meters)):
        meter = users_meters[i]
        print(f"{i + 1}. {meter['alias']}: {meter['meter_number']}")
    
    sleep(1)
    return users_meters
    
def choose_meter(current_user):
    print("\n---- Choose Meter ----")
    print("Type 0 to cancel.")
    
    users_meters = list_meters(current_user)
    
    if len(users_meters) == 0:
        print("You have not added any meters .")
        sleep(1)
        return None
    
    while True:
        choice = input("Select meter number (example: 1): ").strip()
        if choice == "0":
            print("Cancelled.")
            sleep(1)
            return None
        
        if not choice.isdigit():
            print("Invalid choice. Enter a number like 1, 2, 3...")
            sleep(1)
            continue
        
        choice = int(choice)
        
        if choice < 1 or choice > len(users_meters):
            print("Choice out of range.")
            sleep(1)
            continue
        
        """
        The user is choosing human numbering (1, 2, 3, ....) but Python lists use index numbering (0, 1, 2, ...)
        When you print meters, you have:
            1) Home - 111111111111
            2) Shop - 111111111112
            etc.
        That means choice 1) should pick the first item in the list, choice 2) should pick the second item
        But in programming, the first item is users_meters[0], second item is users_meters[1]
        So we subtract 1 to the choice to convert human choice to python index
        -- choice: 1 -> 1 - 1 = 0 -> user_meters[0]
        -- choice: 2 -> 2 - 1 = 1 -> user_meters[1]
        
        """
        
        select_meter = users_meters[choice - 1]
        print(f"Selected meter: {select_meter['alias']}")
        sleep(1)
        
        return select_meter