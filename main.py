from auth import register, login 
def main():
    print("MeterLink CLI")
    print("1) Register ")
    print("2) Login")
    print("3) Exit")
    choice = input("choice: ").strip()

    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Bye")
main()