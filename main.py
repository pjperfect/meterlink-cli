from auth import register, login
from meters import add_meter,list_meters,choose_meter
from purchases import show_purchases, show_total, show_recent
from excel_import import import_excel_for_meter
from time import sleep
import signal

def main():
    #Before login
    current_user = None
    selected_meter = None
    
    while True:
        if current_user is None:
            #log in menu
            print("\n---- Meterlink CLI ----")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choice: ").strip()
           
            if choice == "1":
                register()
            elif choice == "2":
               current_user = login()
               if current_user is None:
                    continue
               selected_meter = None
            elif choice == "3":
                print("You have exited the application.") 
                sleep(1)
                break
            else:
                print("Invalid choice.")   
        else:
            #logged in menu
            username = current_user["username"]
            print(f"\n---- Welcome: {username} ----")
            if selected_meter is None:
                print("Selected Meter: None")
            else:
                print(f"Selected meter: {selected_meter['alias']}")
                
            print("1) Add Meter")
            print("2) List Meters")
            print("3) Choose Meter")   
            print("4) Import Excel (Selected Meter)") 
            print("5) View Purchases (Selected Meter)")
            print("6) Totals (Selected Meter)")
            print("7) Last 5 Purchases (Selected Meter)")
            print("8) Logout")
            
            choice = input("Choice: ").strip()
            
            if choice == "1":
                add_meter(current_user)
            elif choice == "2":
                list_meters(current_user)
            elif choice == "3":
                selected_meter = choose_meter(current_user)
            elif choice == "4":
                import_excel_for_meter(selected_meter)
            elif choice == "5":
                show_purchases(selected_meter)
            elif choice == "6":
                show_total(selected_meter)
            elif choice == "7":
                show_recent(selected_meter)
            elif choice == "8":
                current_user = None
                selected_meter = None
                print("You have logged out.")
                sleep(1)
            else:
                print("Invalid choice.")

# To enable Ctrl + C & Ctrl + D to run also on dist
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        signal.signal(signal.SIGINT, signal.SIG_IGN)  # ignore extra Ctrl+C
        print("\nExiting...")
        try:
            sleep(1)
        except KeyboardInterrupt:
            pass








