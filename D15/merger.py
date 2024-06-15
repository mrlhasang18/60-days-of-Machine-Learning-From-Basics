# Let's create a simple python program to merge pdfs


import PyPDF2

files = ["quote1.pdf","quote2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in files:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
    pdfFile.close()

merger.write("merged_quote.pdf")