# import xlrd
#
# wb = xlrd.open_workbook("C:/Users/LAL KRISHNA/Documents/QSpiders Files Downloaded/MyExcelFile07July/testdata.xlrd")
# ws = wb.sheet_by_name("Sheet1")
# var = ws.cell_value(0,0)
# print(var)

# Read 1st row data
# row_count = ws.nrows
# for i in range(row_count):
#     # print(ws.cell_value(i,0))
#     pass
#
# # Read 1st Column data
# col_count = ws.ncols
# for i in range(col_count):
#     # print(ws.cell_value(0,i))
#     pass

# Read Entire sheet data
# for i in range(row_count):
#     for j in range(col_count):
#         print(ws.cell_value(i,j))

# Depending on user input(col name) >> i should get output
# # # Step1
# for i in range(row_count):
#     for j in range(col_count):
#         if (ws.cell_value(i,j) == "UN"):
#             print(ws.cell_value(i+1, j))        # So we are taking teh next immediate row and get the value of that currespondent column data
#     break                                       # We have to provide the " break" for the "for loop" and not for the if conditoin, # This id for the outer for loop and not for the inner for loop


# # #  Now generalize this method

# # # Read Data method : These methods are called as Utility Method"
# # # web generic method : we use this for Web application related action (Select , submit, click)
# # # the Loc Generic method is for Locators
# import xlrd
# def read_data(Workbook_path, Sheet_name, Column_name ):
#     wb = xlrd.open_workbook(Workbook_path)
#     ws = wb.sheet_by_name(Sheet_name)
#     row_count = ws.nrows
#     col_count = ws.ncols
#
#     for i in range(row_count):
#         for j in range(col_count):
#             if (ws.cell_value(i, j) == Column_name):
#                 print(ws.cell_value(i + 1,
#                                     j))  # So we are taking teh next immediate row and get the value of that currespondent column data
#         break  # We have to provide the " break" for the "for loop" and not for the if conditoin
#
# read_data("C:/Users/LAL KRISHNA/Documents/QSpiders Files Downloaded/MyExcelFile07July/testdata.xlrd", "Sheet1", "UN")
# read_data("C:/Users/LAL KRISHNA/Documents/QSpiders Files Downloaded/MyExcelFile07July/testdata.xlrd", "Sheet1", "PWD")
