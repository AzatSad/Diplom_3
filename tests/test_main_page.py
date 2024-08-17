import allure
from conftest import driver, registration_user_fixture
from constants import USER_DATA
from locators.constants import ORDER_FEED_URL, MAIN_PAGE_URL
from pages.main_page import MainPage


@allure.story('Главная страница')
class TestMainPage:
    @allure.title('Проверить переход на страницу "Лента заказов" по клику на кнопку "Лента заказов"')
    def test_redirect_to_order_feed(self, driver):
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        with allure.step('Проверить совпадение текущего URL с URL "Лента заказов"'):
            assert main_page.get_current_url() == ORDER_FEED_URL

    @allure.title('Проверить переход по клику на "Конструктор"')
    def test_redirect_to_kit_page(self, driver):
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        with allure.step('Клик на кнопку "Конструктор"'):
            main_page.click_to_kit_button()

        with allure.step('Проверить присутствие кнопки "Войти в аккаунт" '):
            text = main_page.get_text_from_login_button()
            assert text == 'Войти в аккаунт'

    @allure.title('Проверить открытие модального окна с деталями при клике на ингредиент')
    def test_show_window_after_click_ingredient(self, driver):
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик по булке "Краторная булка"'):
            main_page.click_by_crator_bun()

        with allure.step('Проверить открытие модального окна "ингредиенты"'):
            text = main_page.get_text_from_ingredient_window()
            assert text == "Детали ингредиента"

    @allure.title('Проверить закрытие модального окна кликом по крестику')
    def test_close_window_after_click_by_cross(self, driver):
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Клик по булке "Краторная булка"'):
            main_page.click_by_crator_bun()

        with allure.step('Клик по крестику в окне "ингредиенты"'):
            main_page.click_by_cross_in_ingredients_window()

        text = main_page.get_text_from_login_button()

        with allure.step('Проверить присутствие кнопки "Войти в аккаунт" '):
            assert text == 'Войти в аккаунт'

    @allure.title('Проверить увеличение счетчика ингредиента при добавлении ингредиента в заказ')
    def test_increasing_ingredient_counter(self, driver):
        main_page = MainPage(driver)

        with allure.step('Перейти на основную страницу'):
            main_page.go_to_site(MAIN_PAGE_URL)

        with allure.step('Добавить флюоресцентную булку в заказ'):
            main_page.add_fluorescent_bun_in_order()

        with allure.step('Проверить количество булок =2'):
            quantity = main_page.count_buns_in_order()
            assert quantity == '2'

    @allure.title('Проверить возможность оформить заказ авторизованным пользователем')
    def test_authorized_user_can_create_order(self, driver, registration_user_fixture):
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

        with allure.step('Получить текста с кнопки "Оформить заказ" и проверить соответствие тексту "Оформить заказ'):
            text = main_page.get_text_from_button_authorized_user()
            assert text == 'Оформить заказ'
