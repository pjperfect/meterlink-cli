import openpyxl

from storage import load_purchases, save_purchases, get_next_id

def import_excel_for_meter(current_user, selected_meter):
    if selected_meter is None:
        print("Select a meter first.")
        return None

    if selected_meter["user_id"] !== current_user["id"]:
        print("This meter is not yours.")
        return None

    file_path = input("Enter your Excel file path (example: Book1.xlsx)")

    workbook = openpyxl.load_workbook(file_path)
    excel_sheet = workbook.active

    purchases_list = load_purchases()

    row = 2
    purchase_date = excel_sheet.cell(row = row, column = 1)
    amount = excel_sheet.cell(row = row, column = 2)
    mpesa_code = excel_sheet.cell(row = row, column = 3)
    message = excel_sheet.cell(row = row, column = 4)

    if purchase_date is None:
        return 0
    if amount is None or mpesa_code is None:
        row = row + 1

    amount_int = float(amount)

    new_purchase = {
        "id": get_next_id(purchases_list),
        "meter_id": selected_meter["id"],
        "amount_float": amount_float,
        "purchase_date": purchase_date,
        "mpesa_code": mpesa_code,
        "message": message
        
    }

    purchases_list.append(new_purchase)
    save_purchases(purchases_list)

    print(f"Imported {row} purchases")
    return row




    