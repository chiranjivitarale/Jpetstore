import pytest
from selenium import webdriver


# from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        # options = Options()
        # options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        # driver = webdriver.Firefox(options=options)
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://petstore.octoperf.com/actions/Account.action?signonForm=")
    yield driver
    driver.quit()