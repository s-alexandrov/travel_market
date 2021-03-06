import random
import allure
from models.register import RegisterUserModel
from fixtures.constants import RegNotice


class TestRegisterPage:
    @allure.feature("register page")
    @allure.story("Успешная регистрация с заполнением всех полей.")
    def test_valid_registration(self, app):
        """
        Успешная регистрация с заполнением всех полей.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        app.register_page.register_user(data=data)
        assert app.register_page.success_log_in_text() == RegNotice.LOG_IN

    @allure.feature("register page")
    @allure.story("Успешная регистрация с заполнением не всех полей.")
    def test_valid_registration_incomplete_data(self, app):
        """
        Успешная регистрация с заполнением не всех полей.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.firstname = None
        data.email = None
        app.register_page.register_user(data=data)
        assert app.register_page.success_log_in_text() == RegNotice.LOG_IN

    @allure.feature("register page")
    @allure.story("Регистрация с разными Password и Password confirmation.")
    def test_invalid_password(self, app):
        """
        Регистрация с разными Password и Password confirmation.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_2 = random.randint(100, 10000)
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD

    @allure.feature("register page")
    @allure.story("Регистрация с некорректным email.")
    def test_invalid_email(self, app):
        """
        Регистрация с некорректным email.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.email = data.domain
        app.register_page.register_user(data=data)
        assert app.register_page.success_log_in_text() != RegNotice.LOG_IN

    @allure.feature("register page")
    @allure.story("Регистрация с некорректным возрастом (меньше 18 лет).")
    def test_invalid_age(self, app):
        """
        Регистрация с некорректным возрастом (меньше 18 лет).
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.age = random.randint(0, 17)
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_AGE

    @allure.feature("register page")
    @allure.story("Регистрация с паролем состоящем только из цифр.")
    def test_password_is_numeric(self, app):
        """
        Регистрация с паролем состоящем только из цифр.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1, data.password_2 = "04725596632", "04725596632"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD_NUMERIC

    @allure.feature("register page")
    @allure.story("Регистрация с простым/распространенным паролем.")
    def test_password_is_common(self, app):
        """
        Регистрация с простым/распространенным паролем.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1, data.password_2 = "password", "password"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_PASSWORD_COMMON

    @allure.feature("register page")
    @allure.story("Повторная регистрация с существующим username в базе данных.")
    def test_re_registration(self, app):
        """
        Повторная регистрация с существующим username в базе данных.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.user = "qwerty"
        app.register_page.register_user(data=data)
        assert app.register_page.error_text() == RegNotice.ERROR_RE_REG
