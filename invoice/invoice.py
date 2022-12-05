import time
from random import choice
import requests
import json
import qrcode
from commodity import Commodity


class Invoice:
    def __init__(self):
        self.invoice_number = 0
        self.payment = 0
        self.payment_in_currency = 0
        self.currency = None
        self.item = 0
        self.account_number = '175422555/3030'
        self.variable_symbol = 0
        self.qr = 0
        self.path_adress_img = ""

    def __str__(self):
        return f"invoice_number = {self.invoice_number} \nitem = {self.item} \npayment = {self.payment} \nvariable_symbol = {self.variable_symbol} \naccount_number = {self.account_number}"

    def generate_variable_symbol(self):
        local = time.localtime()
        part_invoice_number = str(self.invoice_number)[:4]
        self.variable_symbol = f'{part_invoice_number}{str(local[0])[2:]}{local[7]}{local[4]}'

    def generate_invoice_number(self):
        local = time.localtime()
        self.invoice_number = f'{str(local[0])[2:]}{local[7]}{local[3]}{local[4]}{local[5]}'

    def select_item(self):
        product = Commodity()
        self.item = product.select_item()
        self.currency = product.select_currency()
        self.payment_in_currency = product.select_price()
        print(product)

    def calculation_in_cz(self):
        response = requests.get("http://data.kurzy.cz/json/meny/b[1].json")
        py = json.loads(response.text)
        exchange_center = float(f'{py["kurzy"][self.currency]["dev_stred"]}')
        self.payment = self.payment_in_currency * exchange_center

    def entry_in_to_file(self):
        file_with_template = open('templates/template_invoice.html', encoding='utf-8')
        template = file_with_template.read()
        file_with_template.close()

        jmeno_souboru = f'output/invoice_{self.invoice_number}.html'
        with open(jmeno_souboru, mode='w', encoding='utf-8') as sablona:
            print(template.format(nazev_zbozi=self.item,
                                  castka=self.payment_in_currency,
                                  ucet=self.account_number,
                                  var=self.variable_symbol,
                                  adress_img=self.path_adress_img,
                                  cislo_faktury=self.invoice_number),
                  file=sablona)

    def generate_qr_code(self):
        self.path_adress_img = f'img/qr_invoice_{self.invoice_number}.png'
        data = f"invoice_number = {self.invoice_number} \nitem = {self.item} \npayment = {self.payment} \nvariable_symbol = {self.variable_symbol} \naccount_number = {self.account_number}"
        self.qr = qrcode.make(data)
        self.qr.save('output/' + self.path_adress_img)


zkouska = Invoice()
zkouska.select_item()
print(zkouska.product)
print(zkouska.currency)
zkouska.generate_invoice_number()
zkouska.generate_variable_symbol()
zkouska.calculation_in_cz()
zkouska.generate_qr_code()
print(zkouska)
zkouska.entry_in_to_file()

