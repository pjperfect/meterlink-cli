from storage import load_meters, save_meters, get_next_id
from models import Meter

def add_meter(current_user):
    meters_list = load_meters()
    
    meter_number = input("Enter meter number: ")
    
    if meter_number == "":
        print("Meter number cannot be empty.")
        return None
    
    if not meter_number.isdigit():
        print("Meter number must contain digits only.")
        return None
    
    if len(meter_number) != 11 or len(meter_number) != 13:
        print("Meter number must be 11 or 13 digits.")
        return None
    
    for meter in meters_list:
        if meter["user_id"] == current_user["id"] and meter["meter_number"] == meter_number:
            print("Meter already exist.")
            return None
        
    alias = input("Enter alias (example: Home)")
    
    if alias == "":
        print("Alias cannot be empty.")
        return None
    
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
    
    if (users_meters) == 0:
        print("No meter found.")
        return []
    
    for i in range(len(users_meters)):
        meter = users_meters[i]
        print(f"{i + 1} {meter['alias']} -{meter['meter_number']}")
    
    return users_meters
    

def choose_meter(current_user):
    
    users_meters = list_meters(current_user)
    
    if len(users_meters) == 0:
        print("You have not added any meters .")
        return None
    choice = input("Select meter number (example : 1): ")
    if not choice.isdigit():
        print("Invalid choice.")
        return None
    
    choice = int(choice)
    
    if choice < 1 or choice > len(users_meters):
        print("Choice out of range")
        return None
    
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
    print(f"selected meter: {select_meter['alias']}")
    
    return select_meter
