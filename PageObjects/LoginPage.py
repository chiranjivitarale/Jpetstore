# import time

from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class JPeTStore_Login:
    Click_Sing_In_XPATH = (By.XPATH, "//a[normalize-space()='Sign In']")
    Click_Register_now_XPATH = (By.XPATH, "//a[normalize-space()='Register Now!']")
    # User Information
    Text_User_ID_Name = (By.NAME, "username")
    Text_New_Password_Name = (By.NAME, "password")
    Text_Repeat_Password_Name = (By.NAME, "repeatedPassword")
    # Account Information
    Text_First_Name_Name = (By.NAME, "account.firstName")
    Text_Last_Name_Name = (By.NAME, "account.lastName")
    Text_Email_Name = (By.NAME, "account.email")
    Text_Phone_Name = (By.NAME, "account.phone")
    Text_Address_1_Name = (By.NAME, "account.address1")
    Text_Address_2_Name = (By.NAME, "account.address2")
    Text_City_Name = (By.NAME, "account.city")
    Text_State_Name = (By.NAME, "account.state")
    Text_Zip_Name = (By.NAME, "account.zip")
    Text_Country_Name = (By.NAME, "account.country")
    # Profile Information
    DropDown_Language_Preference_XPATH = (By.XPATH, "//select[@name='account.languagePreference']")


    # def Dropdown_Language_Prefence(self, Language):
    #     language = Select(self.driver.find_element(*JPeTStore_Login.DropDown_Language_Preference_XPATH))
    #     language.select_by_visible_text(Language)

    DropDown_Favourite_XPATH = (By.XPATH, "//select[@name='account.favouriteCategoryId']")

    # def Dropdown_Favtrote_Categort(self, Category):
    #     category = Select(self.driver.find_element(*JPeTStore_Login.DropDown_Favourite_XPATH))
    #     category.select_by_visible_text(Category)

    Click_Enable_MyList_XPATH = (By.XPATH, "//input[@name='account.listOption']")
    Click_Enable_MyBanner_XPATH = (By.XPATH, "//input[@name='account.bannerOption']")
    Save_To_Account_info_XPATH = (By.XPATH,"//input[@name='newAccount']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # task poll frequency # default frequency

    # total 10... if the element visible in 3 sec then it will not take complete 10 sec for next operation

    def Click_sing_in(self):
        self.driver.find_element(*JPeTStore_Login.Click_Sing_In_XPATH).click()

    def Click_Register_Now(self):
        self.driver.find_element(*JPeTStore_Login.Click_Register_now_XPATH).click()

    def Enter_Username(self, username):
        self.driver.find_element(*JPeTStore_Login.Text_User_ID_Name).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*JPeTStore_Login.Text_New_Password_Name).send_keys(password)

    def Enter_Repeat_Password(self, Repeatpassword):
        self.driver.find_element(*JPeTStore_Login.Text_Repeat_Password_Name).send_keys(Repeatpassword)

    def Enter_FirstName(self, firstName):
        self.driver.find_element(*JPeTStore_Login.Text_First_Name_Name).send_keys(firstName)

    def Enter_Lastname(self, lastname):
        self.driver.find_element(*JPeTStore_Login.Text_Last_Name_Name).send_keys(lastname)

    def Enter_Email(self, email):
        self.driver.find_element(*JPeTStore_Login.Text_Email_Name).send_keys(email)

    def Enter_Phone(self, phone):
        self.driver.find_element(*JPeTStore_Login.Text_Phone_Name).send_keys(phone)

    def Enter_Address1(self, address1):
        self.driver.find_element(*JPeTStore_Login.Text_Address_1_Name).send_keys(address1)

    def Enter_Address2(self, address2):
        self.driver.find_element(*JPeTStore_Login.Text_Address_2_Name).send_keys(address2)

    def Enter_City(self, city):
        self.driver.find_element(*JPeTStore_Login.Text_City_Name).send_keys(city)

    def Enter_State(self, state):
        self.driver.find_element(*JPeTStore_Login.Text_State_Name).send_keys(state)

    def Enter_Zip(self, Zip):
        self.driver.find_element(*JPeTStore_Login.Text_Zip_Name).send_keys(Zip)

    def Enter_Contry(self, country):
        self.driver.find_element(*JPeTStore_Login.Text_Country_Name).send_keys(country)

    def DropDown_Language_Preference(self, languagePreference):
        language = Select(self.driver.find_element(*JPeTStore_Login.DropDown_Language_Preference_XPATH))
        language.select_by_visible_text(languagePreference)

    def DropDown_Favourite_Category(self, favouritecategory):
        favourite = Select(self.driver.find_element(*JPeTStore_Login.DropDown_Favourite_XPATH))
        favourite.select_by_visible_text(favouritecategory)

    def Click_Enable_MyList(self):
        self.driver.find_element(*JPeTStore_Login.Click_Enable_MyList_XPATH).click()

    def Click_Enable_MyBanner(self):
        self.driver.find_element(*JPeTStore_Login.Click_Enable_MyBanner_XPATH).click()

    def Click_Save_Acount_information(self):
        self.driver.find_element(*JPeTStore_Login.Save_To_Account_info_XPATH).click()



    def Login_Status(self):
        try:
            # self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Menu_XPATH))
            self.driver.find_element(By.XPATH, "//img[@src='../images/logo-topbar.gif']")
            return True
        except:
            return False
