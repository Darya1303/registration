import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.remote import remote_connection



@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome') # use --headless if you do not need a browser ui
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1650,900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)  # usr->local->bin
    return driver

def pytest_addoption(parser):
    """Create options from console for tests env"""
    parser.addoption('--bn', action='store', default="chrome", help="Choose browser: chrome, remote_chrome or firefox")
    parser.addoption('--h', action='store', default="enable", help='Choose headless: enable or other')
    parser.addoption('--s', action='store', default="1920,1080", help='Size window: width,height')
    parser.addoption('--qase_enabled', default="disable", help='Use Qase')
    parser.addoption('--qase_api_token', default=None, help='Qase Api Token')
    parser.addoption('--qase_project_code', default=None, help='Qase project code')
    parser.addini('qase_enabled', default="enable", help='Use Qase')
    parser.addini('qase_api_token', default=None, help='Qase Api Token')
    parser.addini('qase_project_code', default=None, help='Qase project code')

@pytest.fixture(scope="class")
def browser(request):
    if request.config.getoption("bn") == "remote_chrome":
        capabilities = {
            "browserName": "chrome",
            "enableVNC": False,
            "enableVideo": False}
        url = os.environ['SELENOID_URL']
        conn = webdriver.remote.remote_connection.RemoteConnection(url, resolve_ip=False)
        print("\nstart browser for test..")
        driver = webdriver.Remote(command_executor=conn, desired_capabilities=capabilities)
        driver.maximize_window()
        yield driver
        driver.quit()
    elif request.config.getoption("bn") == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()




