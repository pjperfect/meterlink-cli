class User:
    def __init__(self, user_id, username, password_hash, is_locked=False):
        self.id = user_id
        self.username = username
        self.password_hash = password_hash
        self.is_locked = is_locked

    def user_to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash,
            "is_locked": self.is_locked
        }
        


class Meter:
    def __init__(self, meter_id, user_id, meter_number, alias):
        self.id = meter_id
        self.meter_id = meter_id
        self.user_id = user_id
        self.meter_number = meter_number
        self.alias = alias

    def meter_to_dict(self):
        return {
            "id": self.id,
            "meter_id": self.meter_id,
            "user_id": self.user_id,
            "meter_number": self.meter_number,
            "alias": self.alias
        }








class Purchase:
    def __init__(self, purchase_id, meter_id, amount, date_purchase, mpesa_code, message):
        self.id = purchase_id
        self.meter_id = meter_id
        self.amount = amount
        self.date_purchase = date_purchase
        self.mpesa_code = mpesa_code
        self.message = message

    def purchase_to_dict(self):
        return {
            "id": self.id,
            "meter_id": self.meter_id,
            "amount": self.amount,
            "date_purchase": self.date_purchase,
            "mpesa_code": self.mpesa_code,
            "message": self.message
        }
       
