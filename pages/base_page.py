from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        """Переходит на страницу

        Args:
            url: Url страницы

        """
        self.driver.get(url)

    def find_and_click_element(self, locator):
        """Находит элемент по локатору и кликает по нему

        Args:
            locator: Локатор кнопки/элемента

        """
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def input_text(self, locator, text):
        """Вводит значение в поле
        Args:
            locator: Локатор поля ввода
            text: Вводимый текст

        """
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_url(self, expected_url, timeout=30):
        """Ожидает переход на страницу
        Args:
            expected_url: Ожидаемая страница
            timeout: Максимальное время ожидания элемента (в секундах), по умолчанию 30с

        """
        WebDriverWait(
            self.driver, timeout).until(EC.url_to_be(expected_url),
                                        f'URL did not change to {expected_url}')

    def find_element(self, locator, time=20):
        """Находит элемент на странице
        Args:
            locator: Локатор элемента
            time: Максимальное время ожидания элемента (в секундах), по умолчанию 20с

        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def scroll_into_view(self, locator):
        """Перетаскивает элемент со страницы с одного места на другое.

                Args:
                    locator: Локатор элемента

                """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивает элемент со страницы с одного места на другое.

        Args:
            source_locator: Локатор перетаскиваемого элемента
            target_locator: Локатор элемента, на который нужно перетащить исходный элемент

        """
        source_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(source_locator))
        target_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(target_locator))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
