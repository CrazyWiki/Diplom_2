import allure
import requests
import test_data.handlers as Handlers
from test_data.urls import Urls as Urls
from test_data.ingredients import Ingredients

class TestGetUserOrders:
    @allure.title("Проверка получения заказов неавторизованного пользователя")
    @allure.description(
        "Тест проверяет, что неавторизованный пользователь не может получить список заказов и получает статус 401.")
    def test_get_unauthorized_user_orders(self):
        response_get_orders_list = requests.get(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.USER_ORDERS}')
        assert response_get_orders_list.status_code == 401 and response_get_orders_list.json().get("success") == False


    @allure.title("Проверка получения заказов авторизованного пользователя")
    @allure.description("Тест проверяет, что авторизованный пользователь может получить список своих заказов.")
    def test_get_authorized_user_orders(self,create_user_authorization):
        token = {'authorization': create_user_authorization[1]}
        response_create_order = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_ORDER}',data=Ingredients.DATA_INGREDIENT_CORRECT_IDS, headers=token)
        response_get_orders_list = requests.get(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.USER_ORDERS}',headers=token)
        assert response_get_orders_list.json()['orders'][0]['_id']==response_create_order.json()['order']['_id']