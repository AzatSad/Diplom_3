import allure
from conftest import driver, registration_user_fixture
from constants import USER_DATA
from locators.constants import MAIN_PAGE_URL, PROFILE_URL, ORDER_HISTORY_URL, LOGIN_PAGE_URL
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.story('Страница "Профиль"')
class TestProfilePage:
    @allure.title('Проверить переход по клику на "Личный кабинет"')
    def test_click_by_profile_page(self, driver, registration_user_fixture):
        register_user = next(registration_user_fixture)
        user = register_user(USER_DATA)
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_button_personal_account()

        with allure.step('Проверить переход на страниц авторизации'):
            main_page.wait_loading_login_url()

        with allure.step('Заполнить поле "email"'):
            main_page.enter_email_in_login_page(user_data['email'])

        with allure.step('Заполнить поле "пароль"'):
            main_page.enter_password_in_login_page(user_data['password'])

        with allure.step('Клик на кнопку "Войти"'):
            main_page.click_enter_button()

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_profile_button()

        profile_page = ProfilePage(driver)

        with allure.step('Ожидать загрузку страницы "профиль"'):
            profile_page.wait_loading_profile_url()

        with allure.step('Проверить совпадение текущего URL с URL "Профиль"'):
            assert main_page.get_current_url() == PROFILE_URL

    @allure.title('Проверить переход в раздел "История заказов"')
    def test_click_by_orders_story(self, driver, registration_user_fixture):
        register_user = next(registration_user_fixture)
        user = register_user(USER_DATA)
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_button_personal_account()

        with allure.step('Заполнить поле "email"'):
            main_page.enter_email_in_login_page(user_data['email'])

        with allure.step('Заполнить поле "пароль"'):
            main_page.enter_password_in_login_page(user_data['password'])

        with allure.step('Клик на кнопку "Войти"'):
            main_page.click_enter_button()

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_profile_button()

        profile_page = ProfilePage(driver)

        with allure.step('Клик на кнопку "История заказов"'):
            profile_page.click_by_history_button()

        with allure.step('Проверить совпадение текущего URL с URL "История заказов"'):
            assert main_page.get_current_url() == ORDER_HISTORY_URL

    @allure.title('Проверить выход из аккаунта')
    def test_exit_from_account(self, driver, registration_user_fixture):
        register_user = next(registration_user_fixture)
        user = register_user(USER_DATA)
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_button_personal_account()

        with allure.step('Заполнить поле "email"'):
            main_page.enter_email_in_login_page(user_data['email'])

        with allure.step('Заполнить поле "пароль"'):
            main_page.enter_password_in_login_page(user_data['password'])

        with allure.step('Клик на кнопку "Войти"'):
            main_page.click_enter_button()

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_profile_button()

        profile_page = ProfilePage(driver)

        with allure.step('Клик на кнопку "Выход"'):
            profile_page.click_by_exit_button()

        with allure.step('Проверить переход на страниц авторизации'):
            main_page.wait_loading_login_url()

        with allure.step('Проверить совпадение текущего URL с URL "Авторизация"'):
            assert main_page.get_current_url() == LOGIN_PAGE_URL
