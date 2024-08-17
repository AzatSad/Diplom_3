from locators import order_feed_locators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def get_number_of_order_from_order_feed_page(self):
        """Получает номер заказа в статусе "В работе"
        """
        return self.find_element(order_feed_locators.ORDER_NUMBER_FROM_ORDER_FEED_PAGE).text

    def get_information_from_today_counter(self):
        """Получает количество заказов в счетчике "Выполнено за сегодня"
        """
        return self.find_element(order_feed_locators.COUNTER_TODAY_ORDERS).text

    def click_by_kit_button(self):
        """Клик на кнопку "Конструктор"
        """
        self.find_and_click_element(order_feed_locators.BUTTON_KIT)

    def get_text_from_window_with_order_details(self):
        """Получает текст модального окна "Детали заказа
        """
        return self.find_element(order_feed_locators.TEXT_WINDOW_WITH_ORDERS).text

    def click_by_last_order(self):
        """Клик на блок "Последний заказ
        """
        self.find_and_click_element(order_feed_locators.LAST_ORDER_BUTTON)

    def get_information_from_counter(self):
        """Получает количество заказов в счетчике "Выполнено за все время"
        """
        return self.find_element(order_feed_locators.COUNTER_ALL_ORDERS).text

    def get_time_last_order_from_order_feed_page(self):
        """Получает "Время" и "Номер" последнего заказа
        """
        return self.find_element(order_feed_locators.LAST_ORDER).text
