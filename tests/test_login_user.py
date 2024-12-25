import requests
import allure
import test_data.handlers as Handlers
from test_data.user_test_data import UserData
from test_data.urls import Urls as Urls


class TestLoginUser:
    @allure.title("Проверка успешного входа пользователя")
    @allure.description("Тест проверяет успешный вход пользователя с корректными данными.")
    def test_login_user_success(self):
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.LOGIN_USER}',
                                 data=UserData.data_user_exist)
        assert response.json()["success"] == True and response.status_code == 200

    @allure.title("Проверка неуспешного входа пользователя")
    @allure.description("Тест проверяет неуспешный вход пользователя с неправильными данными.")
    def test_login_user_fail(self):
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.LOGIN_USER}',
                                 data=UserData.data_user_fail)
        assert response.json()["success"] == False and response.status_code == 401
