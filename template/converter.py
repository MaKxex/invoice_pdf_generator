import os
from pyhtml2pdf import converter
from Cheetah.Template import Template
from .config import *
import pdfkit

class Converter:
    def __init__(self, template_name:str):
        self.template_filepath = template_dir +"/"+ template_name + ".tmpl"
        self.template = self.__load_template()

    def convert_to_pdf(self,data,pdf_name):
        self.__fill_template_to_html(data)
        return self.__convert_to_pdf(pdf_name)


    def __fill_template_to_html(self,data):
        template_content = self.__load_template()

        # Создаем экземпляр шаблона и заполняем его данными
        print(data.__dict__)
        template = Template(template_content, searchList=[data.__dict__])

        # Получаем заполненный HTML-код
        filled_template = str(template)

        # Сохраняем заполненный шаблон в файл

        with open(html_path, 'w',encoding="utf8") as file:
            file.write(filled_template)

    def __convert_to_pdf(self,filename):
        print("asdasdasdasd")
        print(html_path)
        print(pdfs_dir)
        print(filename)
        converter.convert(f'file:///{html_path}', f'{pdfs_dir}/{filename}.pdf')
        # config = pdfkit.configuration(wkhtmltopdf=wkhtmltox_path)
        # pdfkit.from_file(html_path, f'{pdfs_dir}/{filename}.pdf',configuration=config)
        return f'{pdfs_dir}/{filename}.pdf'

    def __load_template(self) -> Template:
        with open(self.template_filepath, "r",encoding="utf8") as file:
            return file.read()
    



if __name__ == "__main__":

    path = os.path.abspath('template\jur.html')
    converter.convert(f'file:///{path}', 'sample.pdf')