import requests
import pytest
import allure
import test_data.handlers as Handlers
from test_data.urls import Urls as Urls
from test_data.user_test_data import UserData
import test_data.data as Data


class TestCreateUser:
    @allure.title("Проверка успешного создания пользователя")
    @allure.description("Тест проверяет успешное создание пользователя с корректными данными.")
    def test_create_user_success(self):
        data = UserData.data_user_correct
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_USER}', data=data)
        assert response.json().get("success") == True and response.status_code == 200
        token = {'authorization': response.json().get('accessToken')}
        response_delete =  requests.delete(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.USER_INFORMATION}',headers=token)
        assert response_delete.status_code == 202




    @allure.title("Проверка неуспешного создания пользователя с неполными данными")
    @allure.description(
        "Тест проверяет создание пользователя с отсутствующими обязательными полями: email, password и name.")
    @pytest.mark.parametrize('data',[UserData.data_user_without_email,UserData.data_user_without_name,UserData.data_user_without_password])
    def test_create_user_fail_data_not_complete(self,data):
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_USER}', data=data)
        assert response.json()["success"] == False and response.json()["message"] == Data.SERVER_ANSWER_FULL_USER_DATA

    @allure.title("Проверка неуспешного создания пользователя дважды")
    @allure.description("Тест проверяет, что нельзя создать пользователя с уже существующими учётными данными.")
    def test_create_user_twice_fail(self):
        data = UserData.data_user_duplicate
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_USER}', data=data)
        assert response.json()["success"] == False and response.status_code == 403 and response.json()["message"] == Data.SERVER_ANSWER_USER_EXIST
