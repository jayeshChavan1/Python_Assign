# from fpdf import FPDF
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
# pdf.output("simple_demo.pdf")


from pdfdocument.document import PDFDocument

def createPDF(path):
    """
    Create a simple PDF
    """
    pdf = PDFDocument(path)
    pdf.init_report()
    addr = {'first_name':"John", 'last_name':"Hanes",
            'address':"123 Ding Dong Lane",
            'zip_code':"75002", 'city':"Dakota"}
    pdf.address(addr)
    pdf.p("This is a paragraph!")
    pdf.generate()


if __name__ == "__main__":
    createPDF("test.pdf")
