import pytest
import requests

import test_data.handlers as Handlers
from test_data.urls import Urls as Urls
from test_data.user_test_data import UserData


@pytest.fixture(scope='function')
def create_user_authorization():
    data_user = UserData.create_random_data_user()
    response = requests.post(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.CREATE_USER}', data=data_user)
    token = response.json().get('accessToken')
    yield response,token,data_user
    requests.delete(f'{Urls.URL_MAIN_PAGE}{Handlers.Handler.USER_INFORMATION}',headers={'authorization': f'{token}'})
