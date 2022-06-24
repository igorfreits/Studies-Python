"""
PyPDF2 - Unindo e dividindo arquivos PDF
PyPDF2 é uma biblioteca python construída como um kit de ferramentas PDF.
É capaz de:

Extrair informações do documento (título, autor, ...)
Dividir documentos página por página
Mesclar documentos página por página
Cortar páginas
Mesclar várias páginas em uma única página
Criptografar e descriptografar arquivos PDF
e mais!
Documentação:
-https://pythonhosted.org/PyPDF2/

Mais exemplos de uso:
-http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
-https://acervolima.com/trabalhar-com-arquivos-pdf-em-python/

"""
import PyPDF2
import os


# JUNTAS PDFs
way = (r'C:\Users\Igor\Desktop\Estudos\Programação-em-Python'
       r'\Mundo-invertido\Udemy\4-Módulos-Python')

new_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(way):
    for file in files:
        full_path = os.path.join(root, file)

        file_pdf = open(full_path, 'rb')
        new_pdf.append(file_pdf)

with open(f'{way}/new_file.pdf', 'wb') as my_new_pdf:
    new_pdf.write(my_new_pdf)


# SEPARA PDFs
with open(f'{way}/new_file.pdf', 'rb') as file_pdf:
    reader = PyPDF2.PdfFileReader(file_pdf)
    num_pages = reader.getNumPages()

    for num_page in range(num_pages):
        writer = PyPDF2.PdfFileWriter()
        current_page = reader.getPage(num_page)
        writer.addPage(current_page)

        with open(f'{way}/{num_page}.pdf', 'wb') as new_pdf:
            writer.write(new_pdf)
