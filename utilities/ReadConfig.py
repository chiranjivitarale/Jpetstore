import configparser

config = configparser.RawConfigParser()
filepath = "C:\\Users\\USER\\PycharmProjects\\Jpetstore_project\\Configuration\\config.ini"
config.read(filepath)


class Readconfig:
    @staticmethod
    def GetUserName():
        username = config.get('common data', 'Username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common data', 'Password')
        return password

    @staticmethod
    def GetRepeatPassword():
        password = config.get('common data', 'RepeatPassword')
        return password

    @staticmethod
    def FirstName():
        firstname = config.get('common data', 'FirstName')
        return firstname

    @staticmethod
    def LastName():
        lastname = config.get('common data', 'LastName')
        return lastname

    @staticmethod
    def Email():
        email = config.get('common data', 'Email')
        return email

    @staticmethod
    def Phone():
        phone = config.get('common data', 'Phone')
        return phone

    @staticmethod
    def Address1():
        address1 = config.get('common data', 'Address1')
        return address1

    @staticmethod
    def Address2():
        address2 = config.get('common data', 'Address2')
        return address2

    @staticmethod
    def City():
        city = config.get('common data', 'City')
        return city

    @staticmethod
    def State():
        state = config.get('common data', 'State')
        return state

    @staticmethod
    def Zip():
        zip = config.get('common data', 'Zip')
        return zip

    @staticmethod
    def Country():
        country = config.get('common data', 'Country')
        return country






    # state = Select(self.driver.find_element(By.XPATH, "//select[@id='state']"))
    # state.select_by_visible_text("Pune")



