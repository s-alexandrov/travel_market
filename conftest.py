import logging
import pytest
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
        help="travel market",
    ),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    logger.info(f"Start app on {url}")
    chrome_options = Options()
    chrome_options.add_argument("window-size=1800,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    app = Application(driver, url)
    yield app
    app.quit()
