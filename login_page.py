#### Step 15


# # # Step 15   Excel is not working
# from data.jenkins_data import *
# from pages.jenkins_webgeneric import WebGeneric
#
# class Login(WebGeneric):
#     def __init__(self, driver):
#         WebGeneric.__init__(self, driver)
#         self.driver = driver
#         self.un_by_name = "j_username"
#         self.pw_by_name = "j_password"
#         self.loginbutton_by_name = "Submit"
#
#         global wg
#         wg = WebGeneric(driver)
#
#     def enter_user_name(self):
#         Excel_UN = wg.read_data(Workbook_path,Sheet_name, Column_name_UN)
#         wg.enter_value("name", self.un_by_name,Excel_UN)
#         # self.driver.find_element_by_name(self.un_by_name).send_keys(UN)
#         # wg.enter_value("name", self.un_by_name, UN)
#
#
#     def enter_password(self):
#         Excel_UN = wg.read_data(Workbook_path,Sheet_name, Column_name_PWD)
#         wg.enter_value("name", self.un_by_name,Excel_UN)
#         # self.driver.find_element_by_name(self.pw_by_name).send_keys(PW)
#         # wg.enter_value("name", self.pw_by_name, PW)
#
#     def click_signin_button(self):
#         # self.driver.find_element_by_name(self.loginbutton_by_name).click()
#         wg.click_button("name", self.loginbutton_by_name)
#

