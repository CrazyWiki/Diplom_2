import requests
import allure
import test_data.handlers as Handlers
from test_data.urls import Urls as Urls
from test_data.ingredients import Ingredients



class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем с корректными данными')
    @allure.description('Проверяет возможность создания заказа авторизованным пользователем при наличии всех необходимых данных.')
    def test_create_order_authorized_user_correct_data(self, create_user_authorization):
        token = {'authorization': create_user_authorization[1]}
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_ORDER}', data=Ingredients.DATA_INGREDIENT_CORRECT_IDS,headers=token)
        assert response.status_code == 200 and response.json()['order']['_id'] != None

    @allure.title('Создание заказа неавторизованным пользователем с корректными данными')
    @allure.description('Проверяет возможность создания заказа неавторизованным пользователем при наличии всех необходимых данных.')
    def test_create_order_unauthorized_user_correct_data(self):
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_ORDER}', data=Ingredients.DATA_INGREDIENT_CORRECT_IDS)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.title('Создание заказа авторизованным пользователем с пустыми ингредиентами')
    @allure.description('Проверяет, что нельзя создать заказ авторизованным пользователем, если ингредиенты не указаны.')
    def test_create_order_authorized_user_empty_ingredients(self, create_user_authorization):
        token = {'authorization': create_user_authorization[1]}
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_ORDER}', headers=token)
        assert response.status_code == 400 and response.json().get("success") == False

    @allure.title('Создание заказа авторизованным пользователем с неправильным ID ингредиентов')
    @allure.description('Проверяет, что создание заказа авторизованным пользователем с неправильными ID ингредиентов приводит к ошибке.')
    def test_create_order_authorized_user_wrong_ingredients_id(self, create_user_authorization):
        token = {'authorization': create_user_authorization[1]}
        response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_ORDER}', data=Ingredients.DATA_INGREDIENT_INCORRECT_IDS, headers=token)
        assert "Error" in response.text and response.status_code == 500