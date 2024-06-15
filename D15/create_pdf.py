# Let's create a pdf file using python.

# importing 
from fpdf import FPDF

# creating object
a  = FPDF()

# adding page
a.add_page()    
# setting font
a.set_font("Arial", size = 15)

# creating cell
a.cell(200,10,txt = '"The greatest will you can build is',ln = 2, align = "C")
a.cell(200,10,txt = 'the ability to do what you know you need to do,',ln = 3, align = "C")
a.cell(200,10,txt = 'despite how you feel in the moment."',ln = 4, align = "C")


a.output("quote1.pdf")

# creating object for quote2
b  = FPDF()

# adding page
b.add_page()    
# setting font
b.set_font("Arial", size = 15)

# creating cell
b.cell(200,10,txt = '"Believe you can and you\'re halfway there."',ln = 2, align = "C")
b.cell(200,10,txt = '- Theodore Roosevelt',ln = 3, align = "C")


b.output("quote2.pdf")
