import requests

from booking.src.constants.api_constants import BASE_URL, APIConstants, base_url


def test_crud():
    print(BASE_URL)

    url_direc_func = base_url()
    print(url_direc_func)

    requests.get(url=url_direc_func)

    url_class = APIConstants.base_url()
    print(url_class)
