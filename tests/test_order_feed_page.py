import allure
from conftest import driver, registration_user_fixture
from constants import USER_DATA
from locators.constants import MAIN_PAGE_URL
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.story('Страница "Заказы"')
class TestOrderFeedPage:
    @allure.title('Проверить открытие модального окна с деталями при клике на заказ')
    def test_show_details_window(self, driver, registration_user_fixture):
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

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step('Клик на блок "Последний заказа"'):
            order_feed_page.click_by_last_order()

        with allure.step('Получить текст модального окна "Детали заказа" и проверить наличие "Состав"'):
            expected_text = order_feed_page.get_text_from_window_with_order_details()
            assert "Состав" in expected_text

    @allure.title('Проверить увеличение счетчика "Выполнено за всё время" при создании нового заказа')
    def test_all_counter_after_create_new_order(self, driver, registration_user_fixture):
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

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step('Получить количество заказов "Выполнено за все время"'):
            count_orders = int(order_feed_page.get_information_from_counter())

        with allure.step('Клик на кнопку "Конструктор"'):
            order_feed_page.click_by_kit_button()

        with allure.step('Добавить булку "Краторная" в заказ'):
            main_page.add_crator_bun_in_order()

        with allure.step('Клик на кнопку "Оформить заказ"'):
            main_page.click_by_create_order_button()

        with allure.step('Закрыть модальное окно'):
            main_page.click_by_cross_in_modal_window()

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        with allure.step('Получить количество заказов "Выполнено за все время" и проверить увеличение счетчика'):
            new_count_orders = int(order_feed_page.get_information_from_counter())
            assert new_count_orders == count_orders+1

    @allure.title('Проверить увеличение счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_today_counter_after_create_new_order(self, driver, registration_user_fixture):
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

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step('Получить количество заказов "Выполнено за сегодня"'):
            today_orders = int(order_feed_page.get_information_from_today_counter())

        with allure.step('Клик на кнопку "Конструктор"'):
            order_feed_page.click_by_kit_button()

        with allure.step('Добавить булку "Краторная" в заказ'):
            main_page.add_crator_bun_in_order()

        with allure.step('Клик на кнопку "Оформить заказ"'):
            main_page.click_by_create_order_button()

        with allure.step('Закрыть модальное окно'):
            main_page.click_by_cross_in_modal_window()

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        with allure.step('Получить количество заказов "Выполнено за сегодня" и проверить увеличение счетчика'):
            new_today_orders = int(order_feed_page.get_information_from_today_counter())
            assert new_today_orders == today_orders+1

    @allure.title('Проверить появление заказа в разделе "В работе" после оформления')
    def test_status_in_progress_after_create_new_order(self, driver, registration_user_fixture):
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

        with allure.step('Добавить булку "Краторная" в заказ'):
            main_page.add_crator_bun_in_order()

        with allure.step('Клик на кнопку "Оформить заказ"'):
            main_page.click_by_create_order_button()

        with allure.step('Получить номер заказа'):
            number_of_order = main_page.get_number_order_from_window()

        with allure.step('Закрыть модальное окно'):
            main_page.click_by_cross_in_modal_window()

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step('Получить номер заказа в статусе "В работе" и проверить '
                         'соответствие номера оформленного заказа'):
            number_from_status = order_feed_page.get_number_of_order_from_order_feed_page()
            assert number_of_order in number_from_status

    @allure.title('Проверить отображение заказов пользователя на странице "Лента заказов" из раздела "История заказов"')
    def test_similar_order_history(self, driver, registration_user_fixture):
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

        with allure.step('Добавить булку "Краторная" в заказ'):
            main_page.add_crator_bun_in_order()

        with allure.step('Клик на кнопку "Оформить заказ"'):
            main_page.click_by_create_order_button()

        with allure.step('Закрыть модальное окно'):
            main_page.click_by_cross_in_modal_window()

        with allure.step('Клик на кнопку "Лента заказов"'):
            main_page.click_order_list_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step('Получить "Время" и "Номер" последнего заказа'):
            time_from_order_feed_page = order_feed_page.get_time_last_order_from_order_feed_page()

        with allure.step('Клик на кнопку "Личный кабинет"'):
            main_page.click_button_personal_account()

        profile_page = ProfilePage(driver)

        with allure.step('Клик на кнопку "История заказов"'):
            profile_page.click_by_history_button()

        with allure.step('Проскроллить до последнего заказа'):
            profile_page.scroll_to_last_order()

        with allure.step('Получить время оформления последнего заказа "История заказов"'
                         ' и проверить соответствие с временем оформления'):
            time_from_profile_page = profile_page.get_time_last_order_from_profile_page()
            assert time_from_order_feed_page in time_from_profile_page
