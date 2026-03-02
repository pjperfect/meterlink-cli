from time import sleep
from storage import load_purchases, save_purchases, get_next_id
from models import Purchase

def format_date(date_text):
    if date_text is None:
        return ""
    date_text = str(date_text)

    if len(date_text) >= 8 and date_text[0:8].isdigit():
        yyyy = date_text[0:4]
        mm = date_text[4:6]
        dd = date_text[6:8]
        rest = date_text[8:]
        return f"{yyyy}/{mm}/{dd}{rest}"
    return date_text


def add_purchase(current_user, selected_meter):
    # Manual add (optional). You can keep it for testing.

    if selected_meter is None:
        print("Select a meter first.")
        sleep(1)
        return None

    # optional safety check
    if selected_meter["user_id"] != current_user["id"]:
        print("This meter is not yours.")
        sleep(1)
        return None

    purchases_list = load_purchases()

    print("\n---- Add Purchase ----")
    print("Type 0 to cancel.")


    while True:
        date_purchase = input("Enter purchase date (example: 2026-02-24): ").strip()

        if date_purchase == "0":
            print("Cancelled.")
            sleep(1)
            return None

        if date_purchase == "":
            print("Date cannot be empty.")
            sleep(1)
            continue

        break


    while True:
        amount_text = input("Enter amount (KES): ").strip()

        if amount_text == "0":
            print("Cancelled.")
            sleep(1)
            return None

        if not amount_text.isdigit():
            print("Amount must be a number.")
            sleep(1)
            continue

        amount = int(amount_text)

        if amount <= 0:
            print("Amount must be greater than 0.")
            sleep(1)
            continue

        break


    while True:
        mpesa_code = input("Enter mpesa code (or Token): ").strip()

        if mpesa_code == "0":
            print("Cancelled.")
            sleep(1)
            return None

        if mpesa_code == "":
            print("Mpesa code cannot be empty.")
            sleep(1)
            continue

        break


    message = input("Message (optional): ").strip()

    new_id = get_next_id(purchases_list)

    purchase_object = Purchase(
        purchase_id=new_id,
        meter_id=selected_meter["id"],
        amount=amount,
        date_purchase=date_purchase,
        mpesa_code=mpesa_code,
        message=message,
    )

    purchases_list.append(purchase_object.purchase_to_dict())
    save_purchases(purchases_list)

    print("Purchase added.")
    sleep(1)
    return purchase_object.purchase_to_dict()



def get_purchases_for_meter(selected_meter):

    purchases_list = load_purchases()
    meter_purchases = []

    for purchase in purchases_list:
        if purchase["meter_id"] == selected_meter["id"]:
            meter_purchases.append(purchase)

    return meter_purchases



def show_purchases(selected_meter):

    if selected_meter is None:
        print("Select a meter first.")
        sleep(1)
        return []

    meter_purchases = get_purchases_for_meter(selected_meter)

    if len(meter_purchases) == 0:
        print("No purchases found for this meter.")
        sleep(1)
        return []

    print("\n---- Purchases ----")
    for i in range(len(meter_purchases)):
        purchase = meter_purchases[i]
        print(f"{i + 1}) {format_date(purchase['date_purchase'])} | KES {purchase['amount']} | {purchase['mpesa_code']}")
        
    sleep(1)
    return meter_purchases



def show_total(selected_meter):

    if selected_meter is None:
        print("Select a meter first.")
        sleep(1)
        return 0

    meter_purchases = get_purchases_for_meter(selected_meter)

    total = 0
    for purchase in meter_purchases:
        total = total + int(purchase["amount"])

    print(f"\n---- Total ----")
    print(f"Total spent for {selected_meter['alias']}: KES {total}")
    sleep(1)
    return total



def show_recent(selected_meter):

    if selected_meter is None:
        print("Select a meter first.")
        sleep(1)
        return []

    meter_purchases = get_purchases_for_meter(selected_meter)

    if len(meter_purchases) == 0:
        print("No purchases found for this meter.")
        sleep(1)
        return []

    # last 5 purchases
    start_index = 0
    if len(meter_purchases) > 5:
        start_index = len(meter_purchases) - 5

    recent_purchases = meter_purchases[start_index:]

    print("\n---- Recent Purchases ----")
    for purchase in recent_purchases:
        print(f"{format_date(purchase['date_purchase'])} | KES {purchase['amount']} | {purchase['mpesa_code']}")

    sleep(1)
    return recent_purchases