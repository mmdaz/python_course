import xlsxwriter

workbook = xlsxwriter.Workbook("test.xlsx")

worksheet = workbook.add_worksheet("test_worksheet")

worksheet.write("A1", "hello world")

workbook.close()