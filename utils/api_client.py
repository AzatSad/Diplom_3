import allure
import requests
from locators.constants import URL_REGISTRATION, URL_DELETE


class APIClient:
    def __init__(self):
        self.url_registration = URL_REGISTRATION
        self.url_delete = URL_DELETE

    @allure.step('Создать пользователя')
    def create_new_user(self, endpoint, email=None, password=None, name=None):
        url = self.url_registration
        data = {"email": email, "password": password, "name": name}
        response = requests.post(url, json=data)
        return response

    @allure.step('Удалить пользователя')
    def delete_user(self, authorization):
        url = self.url_delete
        headers = {"Authorization": authorization}
        response = requests.delete(url, headers=headers)
        return response
