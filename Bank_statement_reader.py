# Figure out negative numbers when I do the checking/savings account. Have a statement for \-.
# Refomat data so that it doesn't save to excel with a ' in front of every value. ' signifies text.
import openpyxl
import PyPDF2
import re

pdfFileObj = open("/home/cesare/Documents/11_23_17.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pdfReader.numPages ----Reads number of pages...might use later.
pageObj = pdfReader.getPage(2)  # Chooses what page to extract...need to iterate over each page except [1]


def extract_usable_text(bank_statement):

    split_text = bank_statement.split("Description$ Amount", 1)
    shortened_string = str(split_text[1])
    commas_deleted = shortened_string.replace(",", "")
    return commas_deleted


def extract_descriptions(text, dates, dollar_amounts):

    values_replaced = text

    for item in dates:
        if item in text:
            values_replaced = values_replaced.replace(item, "")
    for item in dollar_amounts:
        if item in text:
            values_replaced = values_replaced.replace(item, "XxXxX")
    values_replaced = values_replaced.split("XxXxX")
    values_replaced = values_replaced[:len(values_replaced)-1]
    if "Payment Thank You" in values_replaced[0]:
        first_item = values_replaced[0]
        splitting_value = re.findall("\.\d\d", first_item)
        payment_removed = first_item.split(splitting_value[0], 1)
        string_payment_removed = str(payment_removed[1])
        values_replaced[0] = string_payment_removed

    print(values_replaced)
    return values_replaced


def extract_dollar_amounts(text):

    dollar_amounts = re.findall("\d+\.\d\d", text)

    if "Total interest charged" in text:
        dollar_amounts = dollar_amounts[:len(dollar_amounts)-2]
    if "Payment Thank You" in text:
        dollar_amounts = dollar_amounts[1:]

    print(dollar_amounts)
    return dollar_amounts


def extract_dates(text):

    improper_dates = re.findall("\D\d/\d\d|\D\d\d/\d\d|\d+/\d\d", text)
    shortened_dates = []
    shortened_dates.append(improper_dates[0])

    for item in improper_dates:
        if re.search('[a-zA-Z]', item):
            shortened_dates.append(item[1:])
        else:
            shortened_dates.append(item[2:])
    del shortened_dates[1]
    if "Payment Thank You" in text:
        shortened_dates = shortened_dates[1:]

    print(shortened_dates)
    return shortened_dates


def export_to_excel(dates, descriptions, dollar_amounts):

    wb = openpyxl.load_workbook('/home/cesare/Documents/exported_bank_statement.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')
    row = 1

    for item in dates:
        sheet.cell(row=row, column=1, value=item)
        row += 1
    row = 1
    for item in descriptions:
        sheet.cell(row=row, column=2, value=item)
        row += 1
    row = 1
    for item in dollar_amounts:
        sheet.cell(row=row, column=3, value=item)
        row += 1

    wb.save('/home/cesare/Documents/exported_bank_statement.xlsx')


usable_text = extract_usable_text(pageObj.extractText())
usable_dates = extract_dates(usable_text)
usable_dollar_amounts = extract_dollar_amounts(usable_text)
usable_descriptions = extract_descriptions(usable_text, usable_dates, usable_dollar_amounts)

export_to_excel(usable_dates, usable_descriptions, usable_dollar_amounts)
