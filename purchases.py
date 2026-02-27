from storage import load_purchases, save_purchases, get_next_id
from models import Purchase


def add_purchase(current_user, selected_meter):
    ...
    if selected_meter is None:
        print("Select a meter first.")
        return None

    if selected_meter["user_id"] != current_user["id"]:
        print("This meter is not yours.")
        return None

    purchases_list = load_purchases()

    print("Add Purchase")

    date_purchase = input("Enter purchase date (example: 2026-02-24)").strip()

    if date_purchase == "":
        print("Date cannot be empty.")
        return None

    amount_text = input("Enter amount (KES)")

    if not amount_text.isdigit():
        print("Amount must be a number.")
        return None

    amount = int(amount_text)

    if amount <= 0:
        print("Amount must be greater than 0.")
        return None

    mpesa_code = input("Enter mpesa code (or Token)").strip()

    if mpesa_code == "":
        print("Mpesa code cannot be empty.")
        return None

    message = input("Message (optional)").strip()

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
    return purchase_object.purchase_to_dict()


def get_purchases_for_meter(selected_meter):
    ...
    purchases_list = load_purchases()

    meter_purchases = []

    for purchase in purchases_list:
        if purchase["meter_id"] == selected_meter["id"]:
            meter_purchases.append(purchase)

    return meter_purchases


def show_purchases(selected_meter):
    ...
    if selected_meter is None:
        print("Select a meter first.")
        return []

    meter_purchases = get_purchases_for_meter(selected_meter)

    if len(meter_purchases) == 0:
        print("No purchases found for this meter.")
        return []

    print("Purchases")
    for i in range(len(meter_purchases)):
        purchase = meter_purchases[i]

        print(
            f"{i + 1}) {purchase['date_purchase']} | KES {purchase['amount']} | {purchase['mpesa_code']}"
        )

    return meter_purchases
