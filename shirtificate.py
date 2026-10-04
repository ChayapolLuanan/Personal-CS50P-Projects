# For this problem set, I tried to only import the library fpdf that I have just learned
# because I'm not comfortable with classes yet.

from fpdf import FPDF

def main():
    shirtify(input("Name: "))

def shirtify(n): # "n" stands for "name"
    # This is the so-called "title" of the pdf
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=40)
    pdf.cell(w=0, h=40, txt="CS50 Shirtificate", align="C", ln=1)

    # This is making the shirt stay centered and putting the text on the shirt
    pdf.image("shirtificate.png", x=15, y=70, w=180)
    pdf.set_font("helvetica", style="B", size=28)
    pdf.set_text_color(255, 255, 255)

    # Positioning the text on the shirt and output the PDF file
    pdf.set_y(130)
    pdf.cell(w=0, h=0, txt=f"{n} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
