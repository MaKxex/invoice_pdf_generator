from template.converter import Converter
from datetime import datetime, timedelta


class Item:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.unit = kwargs.get("unit", "Gab.")
        self.quantity = kwargs.get("quantity")
        self.price = kwargs.get("price")
        self.discount = kwargs.get("discount")
        self.total = self.calculate_row_total_price()
        
    def calculate_row_total_price(self):
        return self.price * self.quantity - (self.price * self.quantity * (self.discount / 100))


class TemplateData:
    def __init__(self, **kwargs):
        current_date = datetime.now()
        current_date_plus_week = current_date + timedelta(weeks=1)

        date_stamp_string = current_date.strftime("%d.%m.%Y")
        new_date_stamp_string = current_date_plus_week.strftime("%d.%m.%Y")

        self.money_sign: str = kwargs.get('money_sign', "€")
        self.is_invoice: bool = kwargs.get('is_invoice', "")
        self.is_private: bool = kwargs.get('is_private', "")

        self.document_num: str = kwargs.get('document_num', "")
        self.document_type: str = kwargs.get('document_type', "")
        self.private: str = kwargs.get('private', "")

        self.company_name: str = kwargs.get('company_name', "")
        self.register_number: int = kwargs.get('register_number', 0)
        self.street: str = kwargs.get('street', "")
        self.bank_name: str = kwargs.get('bank_name', "")
        self.bank_index: str = kwargs.get('bank_index', "")
        self.bank_billing: str = kwargs.get('bank_billing', "")

        self.buyer_name: str = kwargs.get('buyer_name', "")
        self.buyer_register_num: int = kwargs.get('buyer_register_num', 0)
        self.buyer_mobile_num: str = kwargs.get('buyer_mobile_num', "")
        self.buyer_email: str = kwargs.get('buyer_email', "")

        self.delivery_type: str = kwargs.get('delivery_type', "")
        self.payment_type: str = kwargs.get('payment_type', "")
        self.shipping_adress: str = kwargs.get('shipping_adress', "")

        self.product_rows: list = kwargs.get('product_rows', [])
        self.temp_price: int = kwargs.get('temp_price', 0)
        self.extras: list = kwargs.get('extras', [])
        self.total_price: int = kwargs.get('total_price', 0)
        self.pay_before_date: str = kwargs.get('pay_before_date', new_date_stamp_string)
        self.dateStamp: str = date_stamp_string

#TODO remake Converter for TemplateData data class
class Doc:
    def __init__(self, DataObject:TemplateData):
        #print(DataObject.__dict__)
        self.dataObj = DataObject
        self.choose_client_type(self.dataObj.is_private)
        self.choose_document_type(self.dataObj.is_invoice)
        self.calculate_temp_price()
        self.calculate_total_price()

        self.pdf_name = self.dataObj.document_type + "_" + self.dataObj.document_num
        print(self.pdf_name)


    def choose_client_type(self,for_private:bool):
        if for_private : #priv
            self.dataObj.private = "private"
            return
        self.dataObj.private = "business"
        
    def choose_document_type(self,is_invoice:bool):
        if is_invoice:
            self.dataObj.document_type = "Rēķins"
            return
        self.dataObj.document_type = "Pavadzīme"

    def calculate_temp_price(self):
        self.dataObj.temp_price = sum([price.total for price in self.dataObj.product_rows])

    def calculate_total_price(self):
        self.dataObj.total_price = self.dataObj.temp_price + sum([values.get("value") for values in self.dataObj.extras])



    def get_pdf(self):
        Converter(self.dataObj.private).convert_to_pdf(self.dataObj,self.pdf_name)
        

if __name__ == "__main__":
    template = TemplateData(
            money_sign="€",

            is_invoice=True,
            is_private=True,

        )
    Doc(template).get_pdf()

    
    
