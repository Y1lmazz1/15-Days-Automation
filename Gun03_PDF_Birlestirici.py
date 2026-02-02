import os
from pypdf import PdfWriter

target_dir = os.path.expanduser("~/Desktop/Deneme_Alani")
output_path = os.path.join(target_dir, "Birlesmis_Dosya.pdf")

def merge_pdfs():
    if not os.path.exists(target_dir):
        return

    merger = PdfWriter()
    pdf_files = [f for f in os.listdir(target_dir) if f.endswith(".pdf")]
    pdf_files.sort()

    if not pdf_files:
        return

    for pdf in pdf_files:
        merger.append(os.path.join(target_dir, pdf))

    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    merge_pdfs()