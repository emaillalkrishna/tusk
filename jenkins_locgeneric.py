# # # Step 15   --> Excel Sheet Not working
# import xlrd
# class LocGeneric:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def locator(self, loc_type, loc_value):
#         try:
#
#             if (loc_type == "name"):
#                 ele = self.driver.find_element_by_name(loc_value)
#                 return ele
#
#             elif (loc_type == "id"):
#                 ele = self.driver.find_element_by_id(loc_value)
#                 return ele
#
#             elif (loc_type == "class_name"):
#                 ele = self.driver.find_element_by_class_name(loc_value)
#                 return ele
#
#             elif (loc_type == "xpath"):
#                 ele = self.driver.find_element_by_xpath(loc_value)
#                 return ele
#
#         except AssertionError as e:
#             print("report fail")
#
#         except:
#             print("fail")
#
# # # # Now place the "read data" Utility method in the Loc Generic
# # # # In data sheet specify the exc el sheet path
# # # # In Page file call the read data method and do the modifications.
#
#     def read_data_login(Workbook_path, Sheet_name, Column_name ):
#         wb = xlrd.open_workbook(Workbook_path)
#         ws = wb.sheet_by_name(Sheet_name)
#         row_count = ws.nrows
#         col_count = ws.ncols
#
#         for i in range(row_count):
#             for j in range(col_count):
#                 if (ws.cell_value(i, j) == Column_name):
#                     print(ws.cell_value(i + 1, j))
#                         # So we are taking teh next immediate row and get the value of that currespondent column data
#             break       # We have to provide the " break" for the "for loop" and not for the if conditoin
