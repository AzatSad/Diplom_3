import allure

from conftest import driver
from pages.recover_password_page import RecoverPasswordPage
from pages.main_page import MainPage
from locators.constants import MAIN_PAGE_URL, RECOVER_PASSWORD_URL, RESET_PASSWORD_URL


@allure.story('Страница "Восстановить пароль"')
class TestRecoverPasswordPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_redirect_from_recovery_password(self, driver):
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_button_personal_account()

        with allure.step('Клик на текст "Восстановить пароль"'):
            main_page.click_text_recover_password()

        with allure.step('Проверить совпадение текущего URL с URL восстановления пароля шаг ввод почты'):
            assert main_page.get_current_url() == RECOVER_PASSWORD_URL

    @allure.title('Проверка перехода на страницу "Восстановление пароля" ввести почту и кликнуть '
                  'по кнопке "Восстановить"')
    def test_entering_mail_and_click_recovery_button(self, driver):
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_button_personal_account()

        with allure.step('Клик на текст "Восстановить пароль"'):
            main_page.click_text_recover_password()

        recover_password_page = RecoverPasswordPage(driver)

        with allure.step('Ввести email в поле "email"'):
            recover_password_page.enter_email_filed('sadertdinov99@gmail.com')

        with allure.step('Клик на кнопку "Восстановить"'):
            recover_password_page.click_recovery_button()

        with allure.step('Ожидать загрузку страницы "Восстановление пароля"'):
            recover_password_page.wait_loading_reset_url()

        with allure.step('Проверить совпадение текущего URL с URL восстановления пароля шаг'
                         ' ввод нового пароля и кода из письма'):
            assert main_page.get_current_url() == RESET_PASSWORD_URL

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_and_hide_password_button(self, driver):
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_button_personal_account()

        with allure.step('Клик на текст "Восстановить пароль"'):
            main_page.click_text_recover_password()

        recover_password_page = RecoverPasswordPage(driver)

        with allure.step('Ввести email в поле "email"'):
            recover_password_page.enter_email_filed('sadertdinov99@gmail.com')

        with allure.step('Клик на кнопку "Восстановить"'):
            recover_password_page.click_recovery_button()

        with allure.step('Клик на кнопку "скрыть" пароль'):
            recover_password_page.click_by_icon_action()

        with allure.step('Проверить видимость значения "Пароль" в поле "Пароль"'):
            status = recover_password_page.get_button_status()
            assert 'input_status_active' in status
