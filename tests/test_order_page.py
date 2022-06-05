import allure

from fixtures.constants import OrderNotice


class TestOrderPage:
    @allure.feature("order page")
    @allure.story("Успешное бронирование отеля.")
    def test_hotel_booking(self, app):
        """
        Успешное бронирование отеля.
        """
        app.order_page.open_login_page()
        app.order_page.login()
        assert app.order_page.success_log_in_text() == OrderNotice.login
        app.order_page.click_button()
        assert app.order_page.find_button_text() == OrderNotice.BUTTON_MORE
        app.order_page.click_button()
        assert app.order_page.find_button_text() == OrderNotice.BUTTON_BOOK
        app.order_page.click_button()
        app.order_page.open_basket_page()
        assert OrderNotice.BOOKED in app.order_page.check_book()
