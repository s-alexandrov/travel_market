import logging
import pytest
import allure
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.app import Application

logger = logging.getLogger("TravelMarket")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://cypress-tourism-app.herokuapp.com/",
        help="Travel Market",
    ),
    parser.addoption("--headless", action="store_true", help="Headless mode"),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    logger.info(f"Start app on {url}")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument("window-size=1800,1080")
    if headless:
        chrome_options.headless = True
    else:
        chrome_options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    app = Application(driver, url)
    yield app
    app.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "app" in item.fixturenames:
                web_driver = item.funcargs["app"].driver
            else:
                logger.error("Fail to take screen-shot")
                return
            web_driver.get_screenshot_as_png()
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name=f'screen-shot_{datetime.datetime.today().strftime("%d-%m-%Y_%H:%M:%S")}',
                attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logger.error("Fail to take screen-shot: {}".format(e))
