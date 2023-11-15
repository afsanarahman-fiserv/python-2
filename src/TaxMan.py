class TaxMan:
    def __init__(self, tax, percent):
        self.tax = tax
        self.percent = float(percent[0:2])/100
        self.total = 0.0

    def calc_total(self):
        new_list = [t["price"] for t in self.tax ]
        for i in new_list:
            self.total += i
        self.total *= (1 + self.percent)

    def get_total(self):
        return round(self.total, 1)