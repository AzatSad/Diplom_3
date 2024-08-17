import allure
from locators import profile_locators
from locators.constants import PROFILE_URL
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def wait_loading_profile_url(self):
        """Ожидает загрузки страницы "Профиль"
        """
        self.wait_for_url(PROFILE_URL)

    def click_by_history_button(self):
        """ Клик на кнопку "История заказов"
        """
        self.find_and_click_element(profile_locators.HISTORY_BUTTON)

    def click_by_exit_button(self):
        """ Клик на кнопку "Выход"
        """
        self.find_and_click_element(profile_locators.EXIT_BUTTON)

    def scroll_to_last_order(self):
        """Скроллит страницу до последнего заказа
        """
        self.scroll_into_view(profile_locators.LAST_ORDER_FROM_HISTORY)

    def get_time_last_order_from_profile_page(self):
        """Получает время оформления последнего заказа в разделе "История заказов"
        """
        return self.find_element(profile_locators.LAST_ORDER_FROM_HISTORY).text
