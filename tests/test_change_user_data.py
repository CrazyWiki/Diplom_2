import requests
import pytest
import allure
import test_data.handlers as Handlers
from test_data.urls import Urls as Urls
from test_data.user_test_data import UserData

class TestChangeUserData:
    @allure.title("Проверка изменения данных неавторизованного пользователя")
    @allure.description("Тест проверяет, что неавторизованный пользователь не может изменить свои данные и получает соответствующее сообщение об ошибке.")
    def test_change_not_authorized_user_data(self):
        response = requests.patch(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.USER_INFORMATION}',
                                  data=UserData.data_updated)
        assert response.json()["message"] == "You should be authorised" and response.status_code == 401

    @allure.title("Проверка изменения данных авторизованного пользователя")
    @allure.description("Тест проверяет, что авторизованный пользователь может корректно изменить свои данные.")
    @pytest.mark.parametrize(
        'new_field, new_value',
        [
            ('password',{'password': UserData.create_random_data_user()['password']}),
            ('email',{'email': UserData.create_random_data_user()['email']}),
            ('name', {'name': UserData.create_random_data_user()['name']})
        ]
    )
    def test_change_authorized_user_data(self, create_user_authorization, new_field, new_value):
        #new_password = {'password': UserData.create_random_data_user()['password']}
        token = {'authorization': create_user_authorization[1]}
        response = requests.patch(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.USER_INFORMATION}', data=new_value,
                                  headers=token)
        assert response.status_code == 200 and response.json().get("success") == True
