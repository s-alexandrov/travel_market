from fixtures.pages.register_page import RegisterPage


class Application:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.register_page = RegisterPage(self)

    def quit(self):
        self.driver.quit()
