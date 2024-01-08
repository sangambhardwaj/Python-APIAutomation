# To Make the POST, PUT, PATCH, DELETE, GET
import requests

from fake_stone_api.src.constrants.api_testdata import APITestData


# HTTP Methods - Generic Functions
class RequestWrapper:

    testdata = APITestData()

    def requester(self, method, url, json=None, params=None):
        if method =="get":
            return requests.get(url=url, params=params)
        elif method == "post":
            return requests.post(url=url, json=json)
        elif method == "put":
            return requests.put(url=url,json=json)
        elif method == "patch":
            return requests.patch(url=url,json=json)
        elif method == "delete":
            return requests.delete(url=url)
        else:
            return "Method not valid"
