import os
from PyPDF2 import PdfMerger
from PIL import Image

def convert_image_to_pdf(image_path, pdf_path):
    img = Image.open(image_path)
    pdf_bytes = img.convert("RGB").save(pdf_path, "PDF", resolution=100.0)

def merge_all_files_to_pdf(input_dir, output_pdf):
    pdf_merger = PdfMerger()
    file_number = 0
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            pdf_path = os.path.splitext(file_path)[0] + ".pdf"
            convert_image_to_pdf(file_path, pdf_path)
            pdf_merger.append(pdf_path)
            file_number += 1
            print(file_number)
        elif file_name.lower().endswith('.pdf'):
            pdf_merger.append(file_path)
            file_number += 1
            print(file_number)
    pdf_merger.write(output_pdf)
    pdf_merger.close()
    print(file_number)

# Specify the input directory containing PDF, JPG, and PNG files
input_dir = "Certificate"

# Specify the output PDF file
output_pdf = "output.pdf"

merge_all_files_to_pdf(input_dir, output_pdf)
