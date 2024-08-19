from locators import main_locators
from locators.constants import LOGIN_PAGE_URL
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_by_create_order_button(self):
        """Клик на кнопку "Оформить заказ"
        """
        self.find_and_click_element(main_locators.CREATE_ORDER_BUTTON)

    def enter_email_in_login_page(self, email):
        """Заполняет поле "email"
        """
        self.find_and_click_element(main_locators.EMAIL_FILED).send_keys(email)

    def click_button_personal_account(self):
        """Клик на кнопку "Личный кабинет"
        """
        self.find_and_click_element(main_locators.BUTTON_PERSONAL_ACCOUNT)

    def click_profile_button(self):
        """Клик на кнопку "Личный кабинет"
        """
        self.find_and_click_element(main_locators.PROFILE_BUTTON)

    def click_by_cross_in_modal_window(self):
        """Закрывает модальное окно
        """
        self.find_and_click_element(main_locators.CLOSE_WINDOW)

    def click_text_recover_password(self):
        """Клик на текст "Восстановить пароль"
        """
        self.find_and_click_element(main_locators.TEXT_RECOVERY)

    def enter_password_in_login_page(self, password):
        """Заполняет поле "пароль"

        Args:
            password: Пароль пользователя

        """
        self.find_and_click_element(main_locators.PASSWORD_FILED).send_keys(password)

    def click_enter_button(self):
        """Клик на кнопку "Войти"
        """
        self.find_and_click_element(main_locators.ENTER_BUTTON)

    def click_by_crator_bun(self):
        """Клик по булке "Краторная булка"
        """
        self.find_and_click_element(main_locators.CRATOR_BUN)

    def get_text_from_ingredient_window(self):
        """Получает текст всплывающего окна "ингредиенты"
        """
        return self.find_element(main_locators.TEXT_DETAIL_INGREDIENTS).text

    def click_to_kit_button(self):
        """Клик на кнопку "Конструктор
        """
        self.find_and_click_element(main_locators.KIT_BUTTON)

    def get_number_order_from_window(self):
        """Получает номер заказа
        """
        return self.find_element(main_locators.ORDER_NUMBER).text

    def add_crator_bun_in_order(self):
        """Добавляет "Краторную" булку в заказ
        """
        self.drag_and_drop(main_locators.CRATOR_BUN, main_locators.ADD_INGREDIENT_IN_ORDER)

    def click_order_list_button(self):
        """Клик на кнопку "Лента заказов
        """
        self.find_and_click_element(main_locators.ORDER_LIST_BUTTON)

    def get_text_from_login_button(self):
        """Возвращает текст кнопки "Войти в аккаунт"
        """
        return self.find_element(main_locators.LOGIN_BUTTON).text

    def get_current_url(self):
        """Получает текущий URL
        """
        return self.driver.current_url

    def add_fluorescent_bun_in_order(self):
        """Добавляет флюоресцентную булку в заказ
        """
        self.drag_and_drop(main_locators.FLUORESCENT_BUN, main_locators.ADD_INGREDIENT_IN_ORDER)

    def wait_loading_login_url(self):
        """Ожидает загрузку страницы "Авторизация"
        """
        self.wait_for_url(LOGIN_PAGE_URL)

    def click_by_cross_in_ingredients_window(self):
        """Клик по крестику в модальном окне "ингредиенты"
        """
        self.find_and_click_element(main_locators.CLOSE_WINDOW)

    def get_text_from_button_authorized_user(self):
        """Получает текст кнопки "Оформить заказ"
        """
        return self.find_element(main_locators.CREATE_ORDER_BUTTON).text

    def count_buns_in_order(self):
        """Подсчитывает количество добавленных булок
        """
        return self.find_element(main_locators.COUNTER_BUN).text
