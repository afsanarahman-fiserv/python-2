class Invoice:
    def __init__(self, data):
        tokens = data.split(",")
        self.id = tokens[0]
        self.user_id = tokens[1]
        self.amount = tokens[2]
        self.paid = tokens[3]

    def __repr__(self):
        return f"Invoice(invoice_id='{self.id}', user_id='{self.user_id}', amount='{self.amount}', paid='{self.paid}')"