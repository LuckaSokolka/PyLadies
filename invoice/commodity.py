from random import choice

options_items = ['Notebook', 'Television', 'Mobile phone']
options_currency = ["EUR", "USD"]
price_in_eur = (551.71, 483.84, 1454.41)
price_in_usd = (299.99, 569.99, 389.00)


class Commodity:
    def __init__(self):
        self.item = 0
        self.price = 0
        self.currency = 0

    def __str__(self):
        return f"{self.item} \n{self.price} \n{self.currency}"

    def select_item(self):
        self.item = choice(options_items)

    def select_currency(self):
        self.currency = choice(options_currency)

    def select_price(self):
        if self.currency == "EUR":
            self.price = choice(price_in_eur)
        elif self.currency == "USD":
            self.price = choice(price_in_usd)


"""zbozi = Commodity()
zbozi.select_item()
zbozi.select_currency()
zbozi.select_price()
print(zbozi)"""
