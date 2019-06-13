import psycopg2
from fpdf import FPDF

connection = psycopg2.connect(user = "postgres",
                              database = "python"
                              )

mycursor = connection.cursor()


psql_select_Query = "select * from demo1"
mycursor.execute(psql_select_Query)

records = mycursor.fetchall()

class PDF(FPDF):

    def header(self):

        self.set_font('Arial','B',22)
        self.cell(0, 15, 'NeoSOFT Technologies', ln=1, align="C")
        self.ln(5)

        self.set_font('Arial','B',15)
        self.cell(0, 5, 'Rabale, Navi Mumbai', ln=1, align="C")
        self.ln(10)

    def footer(self):

        self.set_y(-15)
        self.set_font("Arial", style="I", size=10)
        pageNum = "Page %s" % self.page_no()
        self.cell(0, 12, pageNum, align="C")

    def simple_pdf(spacing=1):

        pdf.set_font("Arial", size=14)
        col_width = pdf.w / 3.3
        row_height = pdf.font_size + 3
        head = ["ID","Name","City"]
        for item in head:
            pdf.cell(col_width, row_height, txt=item, border=1, align="C")
        pdf.ln(row_height)

        for row in records:
            for item in row:
                pdf.cell(col_width, row_height, txt=item, border=1, align="C")
            pdf.ln(row_height)

        pdf.output('pdf_tab.pdf')

pdf = PDF()
pdf.add_page()
pdf.simple_pdf()
