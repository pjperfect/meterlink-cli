from auth import register, login
from meters import add_meter,list_meters,choose_meter
from purchases import get_purchases_for_meter,show_purchases
from excel_import import import_excel_for_meter

def main():
    #Before login
    current_user = None
    selected_meter = None
    
    while True:
        if current_user is None:
            #log in menu
            print("Meterlink CLI")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choice:").strip()
           
            if choice == "1":
                register()
            elif choice == "2":
               current_user = login()
            elif choice == "3":
                print("You have exited the application.") 
                break
            else:
                print("Invalid choice.")   
        else:
            #logged in menu
            username = current_user["username"]
            print(f"Welcome:" , username)
            if selected_meter is None:
                print("Selected Meter: None")
            else:
                print(f"Selected meter:{selected_meter['alias']}")
                
            print("1) Add Meter")
            print("2) List Meters")
            print("3) Choose Meter")   
            print("4) Import Excel") 
            print("5) View Purchases")
            print("6) Logout")
            
            choice = input("Choice:").strip()
            
            if choice == "1":
                add_meter(current_user)
            elif choice == "2":
                list_meters(current_user)
            elif choice == "3":
                selected_meter = choose_meter(current_user)
            elif choice == "4":import_excel_for_meter(current_user, selected_meter)
            elif choice == "5": show_purchases(selected_meter)
            elif choice == "6":
                 current_user = None
                 selected_meter = None
                 print("You have logged out.")
            else:
                print("Invalid choice.")
                
main()                
                
                
                    
            
               
                


