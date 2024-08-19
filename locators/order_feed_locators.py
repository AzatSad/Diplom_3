from selenium.webdriver.common.by import By

LAST_ORDER_BUTTON = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"][1]') # Кнопка "Последний заказ"
CREATE_ORDER_STATUS = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]") # Статус "Ваш заказ готовится"
COUNTER_ALL_ORDERS = (By.CSS_SELECTOR, 'div.undefined.mb-15 p.OrderFeed_number__2MbrQ.text.text_type_digits-large') # Счётчик заказов "Выполнено за всё время"
COUNTER_TODAY_ORDERS = (By.CSS_SELECTOR, 'p.OrderFeed_number__2MbrQ.text.text_type_digits-large') # Счётчик заказов "Выполнено за сегодня"
BUTTON_KIT = (By.XPATH, "//p[contains(text(),'Конструктор')]") # Кнопка "Конструктор"
TEXT_WINDOW_WITH_ORDERS = (By.XPATH, "//p[contains(text(),'Cостав')]") # Модальное окно с деталями заказа
ORDER_NUMBER_FROM_ORDER_FEED_PAGE = (By.CSS_SELECTOR, 'li.text.text_type_digits-default.mb-2') # Номер заказа в работе
LAST_ORDER = (By.XPATH, "//p[@class='text text_type_main-default text_color_inactive'][1]") # Время/номер заказа на странице заказов