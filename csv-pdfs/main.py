# import csv
# data = open('example.csv')
# csv_data = csv.reader(data)
#
# data_lines = list(csv_data)
#
# for row in data_lines[1:5]:
#     print(row[3])

import PyPDF2
# f = open('Working_Business_Proposal.pdf', 'rb')
# pdf_reader = PyPDF2.PdfReader(f)
# print(len(pdf_reader.pages))
#
# first_page = pdf_reader.pages[0]
# print(first_page.extract_text())
# f.close()

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
print(len(pdf_reader.pages))

first_page = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)

pdf_output = open('Some.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()