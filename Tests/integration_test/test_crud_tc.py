import requests
from source.constrants.api_constants import BASE_URL, APIConstants, base_url


def test_crud():
    print(BASE_URL)

    url_direc_func = base_url()
    print(url_direc_func)

    # requests.get()

    url_class = APIConstants.base_url()
    print(url_class)
