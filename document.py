from template.converter import Converter


class TemplateData(NamedTuple):
    document_type: str
    company_name:str
    register_number:int
    street:str
    bank_index:str
    bank_billing:str

    buyer_name:str
    buyer_register_num:int
    buyer_mobile_num:str
    buyer_email:str

    delivary_type:str
    payment_type:str
    shipping_adress:str

    product_rows: list
    temp_price:int
    extras:list
    total_price:int
    pay_before_date:str
    dateStamp:str

#TODO remake Converter for TemplateData data class
class Converter:
    def __init__(self, document_type:int, pdf_name:str):
        self.document_type = document_type # 0 - Rekins, 1- Pavadzime
        self.pdf_name = pdf_name

        self.template_name = self.choose_client_type(self.document_type)

    def choose_client_type(self,for_private:bool):
        if for_private : #priv
            return "private"
        return "business"
        
    def choose_document_type(self,is_invoice:bool):
        if is_invoice:
            return "Reķinš"
        return "Pavadzīme"


        

    def get_pdf(self,data:dict):
        Converter(self.template_name).convert_to_pdf(data,self.pdf_name)
        

if __name__ == "__main__":
    pass
    # Doc(0,"testtesttest").get_pdf(data)

    
    
