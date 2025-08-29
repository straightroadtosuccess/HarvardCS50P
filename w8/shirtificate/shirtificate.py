from fpdf import FPDF

# Get input from user
name = input("Name: ")

# Create PDF object
pdf = FPDF(orientation="P", format="A4")
# Disable page breaks
pdf.set_auto_page_break(auto=False)
# Add new page
pdf.add_page()

# Font formatting
pdf.set_font("Helvetica", size=24)
# Center the title
pdf.cell(w=0, h=20, txt="CS50 Shirtificate", align="C")

# Add shirt image and center
page_width = pdf.w
image_width = 100
x = (page_width - image_width) / 2
pdf.image("shirtificate.png", x=x, y=40, w=image_width)

# Add user name overlayed on shirt
pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", "B", 16)
# Place above shirt image
pdf.set_xy(x, 70)
pdf.cell(w=image_width, h=10, txt=f"{name} took CS50", align="C")

# Save the new file
pdf.output("shirtificate.pdf")
