import allure

from fixtures.constants import LoginNotice


class TestLoginPage:
    @allure.feature("login page")
    @allure.story("Успешная авторизация с валидными данными.")
    def test_successful_login(self, app):
        """
        Успешная авторизация с валидными данными.
        """
        app.login_page.open_login_page()
        app.login_page.entry_data_login()
        assert app.login_page.success_log_in_text() == LoginNotice.login

    @allure.feature("login page")
    @allure.story("Попытка авторизации зарегистрированного пользователя с неверным паролем.")
    def test_login_with_invalid_password(self, app):
        """
        Попытка авторизации зарегистрированного пользователя с неверным паролем.
        """
        app.login_page.open_login_page()
        LoginNotice.password = "1234"
        app.login_page.entry_data_login()
        assert app.login_page.error_text() == LoginNotice.ERROR_LOGIN

    @allure.feature("login page")
    @allure.story("Попытка авторизации незарегистированного пользователя.")
    def test_non_existent_user(self, app):
        """
        Попытка авторизации незарегистированного пользователя.
        """
        app.login_page.open_login_page()
        LoginNotice.login = "qw"
        LoginNotice.password = "353453534"
        app.login_page.entry_data_login()
        assert app.login_page.error_text() == LoginNotice.ERROR_LOGIN

    @allure.feature("login page")
    @allure.story("Попытка авторизации с незаполненым логином.")
    def test_login_with_empty_username(self, app):
        """
        Попытка авторизации с незаполненым логином.
        """
        app.login_page.open_login_page()
        LoginNotice.login = None
        app.login_page.entry_data_login()
        assert app.login_page.index_page_text() != LoginNotice.login

    @allure.feature("login page")
    @allure.story("Попытка авторизации с незаполненым паролем.")
    def test_login_with_empty_password(self, app):
        """
        Попытка авторизации с незаполненым паролем.
        """
        app.login_page.open_login_page()
        LoginNotice.password = None
        app.login_page.entry_data_login()
        assert app.login_page.index_page_text() != LoginNotice.login

    @allure.feature("login page")
    @allure.story("Попытка авторизации с незаполненым логином и паролем.")
    def test_login_with_empty_login_password(self, app):
        """
        Попытка авторизации с незаполненым логином и паролем.
        """
        app.login_page.open_login_page()
        LoginNotice.login = None
        LoginNotice.password = None
        app.login_page.entry_data_login()
        assert app.login_page.index_page_text() != LoginNotice.login
