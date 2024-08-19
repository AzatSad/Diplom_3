from selenium.webdriver.common.by import By

BUTTON_RECOVERY = (By.XPATH, "//button[text()='Восстановить']") # Кнопка "Восстановить"
EMAIL_FIELD = (By.XPATH, "//label[text()='Email']//following-sibling::input[@name='name']") # Поле "Email"
SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]") # Кнопка "Сохранить"
VIEW_PASSWORD = (By.XPATH, "//div[contains(@class, 'input_type_text') and contains(@class, 'input_status_active')]") #  Отобразить пароль
ICON_ACTION = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]") # Кнопка "Скрыть отображение пароля"