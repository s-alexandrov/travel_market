from fixtures.pages.register_page import RegisterPage
from fixtures.pages.login_page import LoginPage


class Application:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.register_page = RegisterPage(self)
        self.login_page = LoginPage(self)

    def quit(self):
        self.driver.quit()
