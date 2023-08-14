# import time

# import allure
# from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import JPeTStore_Login
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig


class Test_Login:
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()
    RepeatPassword = Readconfig.GetRepeatPassword()
    FirstName = Readconfig.FirstName()
    LastName = Readconfig.LastName()
    Email = Readconfig.Email()
    Phone = Readconfig.Phone()
    Address1 = Readconfig.Address1()
    Address2 = Readconfig.Address2()
    City = Readconfig.City()
    State = Readconfig.State()
    Zip = Readconfig.Zip()
    Country = Readconfig.Country()
    log = LogGenerator.loggen()

    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.link("https://petstore.octoperf.com/actions/Catalog.action")
    # @allure.title(" Page Title Test Case")
    # @allure.issue("1234")
    # @allure.story(" This is story#01")
    def test_page_title_001(self, setup):
        self.log.info("Testcase test_page_title_001 is start")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lp = JPeTStore_Login(self.driver)
        self.log.info("Click on Sing in")
        self.lp.Click_sing_in()
        self.log.info("Click on Register now")
        self.lp.Click_Register_Now()
        self.log.info("Entering Username")
        self.lp.Enter_Username(self.Username)
        self.log.info("Entering Password")
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering RepeatPassword")
        # time.sleep(3)
        self.lp.Enter_Repeat_Password(self.RepeatPassword)
        self.lp.Enter_FirstName(self.FirstName)
        self.log.info("Entering Firstname")
        self.lp.Enter_Lastname(self.LastName)
        self.log.info("Entering Lastname")
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Email")
        self.lp.Enter_Phone(self.Phone)
        self.log.info("Entering Phone")
        self.lp.Enter_Address1(self.Address1)
        self.log.info("Entering Address1")
        self.lp.Enter_Address2(self.Address2)
        self.log.info("Entering Address2")
        self.lp.Enter_City(self.City)
        self.log.info("Entering City")
        self.lp.Enter_City(self.State)
        self.log.info("Entering State")
        self.lp.Enter_Contry(self.Country)
        self.log.info("Entering Country")
        self.lp.DropDown_Language_Preference("english")
        self.log.info("Select English")
        self.lp.DropDown_Favourite_Category("CATS")
        self.log.info("Select Cats")
        self.lp.Click_Enable_MyList()
        self.log.info("Click Mylist")
        self.lp.Click_Enable_MyBanner()
        self.log.info("Click MyBanner")
        self.lp.Click_Save_Acount_information()
        self.log.info("Save Account information")

        # if self.lp.Login_Status() == True:
        #     self.log.info("Taking Screenshrt")
        #     self.driver.save_screenshot("C:\\Users\\USER\\PycharmProjects\\Jpetstore_project\\sceernshorts"
        #                                 "\\test_page_title_001_pass")
        #     assert True
        # else:
        #     self.log.info("Taking Screenshrt")
        #     self.driver.save_screenshot("C:\\Users\\USER\\PycharmProjects\\Jpetstore_project\\sceernshorts"
        #                                 "\\test_page_title_001_fail")
        #     assert False
        def Login_Status(self):
            try:
                # self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Menu_XPATH))
                self.log.info("Taking Screenshrt")
                self.driver.save_screenshot("C:\\Users\\USER\\PycharmProjects\\Jpetstore_project\\sceernshorts"
                                                "\\test_page_title_001_pass")
                self.driver.find_element(By.XPATH, "//img[@src='../images/logo-topbar.gif']")
                return True
            except:
                return False
        self.log.info("Tasecase is Completed")
