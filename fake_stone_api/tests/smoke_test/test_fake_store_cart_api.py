from fake_stone_api.src.constrants.api_testdata import APITestData
from fake_stone_api.src.helpers.api_request_wrapper import RequestWrapper
from fake_stone_api.src.constrants.response import ApiResponse
from fake_stone_api.src.constrants.payload_data import ApiPayloadData
from fake_stone_api.src.constrants.params import Param


class TestFakeStoreCartProductsAPIs:

    param = Param()
    payload_data = ApiPayloadData()
    response_data = ApiResponse()
    testdata = APITestData()
    request_wrapper = RequestWrapper()



    def test_001_get_all_cart_product(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.CARTs_URL)
        assert response.status_code == 200


        assert response.json() == self.testdata.json_obj

    def test_002_get_single_cart_product(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.CARTs_URL + "/5")
        assert response.status_code == 200
        assert response.json() == self.testdata.json_obj[4]

    def test_003_limit_and_sort_cart_products(self):

        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.CARTs_URL,
                                                  params=self.param.param)
        assert response.status_code == 200
        # assert "2" in response.json()["id"]
        # for i in range(0, self.param.cart_limit):
             # assert i + 1 == response.json()[self.testdata.json_obj[i]["id"]]

    def test_004_add_product_in_cart(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.POST,
                                                  url=self.testdata.CARTs_URL,
                                                  json=self.payload_data.POST_PAYLOAD)

        assert response.status_code == 200
        assert response.json()["id"] == 11

    def test_005_get_cart_in_range(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.CARTs_URL,
                                                  params=self.param.range_param)
        assert response.status_code == 200
        assert response.json()[0]["id"] == 1

    def test_006_get_user_details_in_cart(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.CART_GET_USER_URL)
        assert response.status_code == 200
        assert response.json()[0]["id"] == 3

    def test_006_update_product_in_cart(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.PUT,
                                                  url=self.testdata.CARTs_URL + "/7",
                                                  json=self.payload_data.UPDATE_CART_DETAILS)
        assert response.status_code == 200
        assert response.json() == self.response_data.UPDATED_CART_PRODUCT_RESPONSE

    def test_007_partial_update_cart(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.PATCH,
                                                  url=self.testdata.CARTs_URL + "/7",
                                                  json=self.payload_data.PARTIAL_UPDATE_CART_DETAILS)
        assert response.status_code == 200
        assert response.json() == self.response_data.PARTIAL_UPDATED_CART_PRODUCT_RESPONSE

    def test_008_delete_product_from_cart(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.DELETE,
                                                  url=self.testdata.CARTs_URL + "/6")
        assert response.status_code == 200



