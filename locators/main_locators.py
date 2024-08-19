from selenium.webdriver.common.by import By

BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка "Личный кабинет"
KIT_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]") # Кнопка "Конструктор"
TEXT_RECOVERY = (By.XPATH, "//a[@href='/forgot-password']") # Текст "Восстановить пароль"
EMAIL_FILED = (By.XPATH, "//label[text()='Email']//following-sibling::input[@name='name']") # Поле "email"
PASSWORD_FILED = (By.XPATH, "//label[text()='Пароль']//following-sibling::input[@name='Пароль']") # Поле "пароль"
ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # Кнопка "Войти"
PROFILE_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # Кнопка "Личный кабинет"
CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # Кнопка "Оформить заказ"
CLOSE_WINDOW = (By.XPATH, '//*[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]') # Кнопка "Закрыть" модальное окно с заказами
ORDER_LIST_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]") # Кнопка "Лента заказов"
CRATOR_BUN = (By.XPATH, "//p[contains(text(),'Краторная булка N-200i')]") # "Краторная булка"
ADD_INGREDIENT_IN_ORDER = (By.XPATH, "//span[contains(text(),'Перетяните булочку сюда (верх)')]") # Элемент "Составить бургер"
ORDER_NUMBER = \
    (By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8") # Номер заказа
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") # Кнопка "Войти в аккаунт"
TEXT_DETAIL_INGREDIENTS = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]") # Текст "детали ингредиента" в всплывающем окне
COUNTER_BUN = (By.XPATH, './/p[@class = "counter_counter__num__3nue1"]') # "Счётчик" количества булок
FLUORESCENT_BUN = (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]") # "Флюоресцентная булка"
