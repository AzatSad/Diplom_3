import allure
from locators import recover_password_locators
from pages.base_page import BasePage
from locators.constants import RESET_PASSWORD_URL


class RecoverPasswordPage(BasePage):
    def enter_email_filed(self, email):
        """Вводит email в поле "email"

        Args:
            email: Почта пользователя

        """
        self.input_text(recover_password_locators.EMAIL_FIELD, email)

    def click_recovery_button(self):
        """Клик по кнопке "Восстановить"
        """
        self.find_and_click_element(recover_password_locators.BUTTON_RECOVERY)

    def click_by_icon_action(self):
        """Клик по кнопке "скрыть" пароль
        """
        self.find_and_click_element(recover_password_locators.ICON_ACTION)

    def wait_loading_reset_url(self):
        """Ожидает загрузку страницы "Восстановление пароля"
        """
        self.wait_for_url(RESET_PASSWORD_URL)

    @allure.step('Получить статус кнопки "скрыть" пароль')
    def get_button_status(self):
        """Получает статус кнопки "скрыть" пароль
        """
        return self.find_element(recover_password_locators.VIEW_PASSWORD).get_attribute("class")
