import os
from fpdf import FPDF

def convert_txt_to_pdf(txt_file_path, pdf_file_path):
    with open(txt_file_path, 'r') as txt_file:
        txt_content = txt_file.read()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt_content)

    pdf.output(pdf_file_path)

    print(f"Converted {txt_file_path} to {pdf_file_path}")

def main():
    folder_path = "C:/sandsresult/"

    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            txt_file_path = os.path.join(folder_path, filename)
            pdf_file_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".pdf")

            convert_txt_to_pdf(txt_file_path, pdf_file_path)

if __name__ == "__main__":
    main()