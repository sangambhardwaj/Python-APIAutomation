from fake_stone_api.src.constrants.api_testdata import APITestData
from fake_stone_api.src.helpers.api_request_wrapper import RequestWrapper
from fake_stone_api.src.constrants.response import ApiResponse
from fake_stone_api.src.constrants.payload_data import ApiPayloadData


class TestFakeStoreProductsAPIs:
    payload_data = ApiPayloadData()
    response_data = ApiResponse()
    testdata = APITestData()
    request_wrapper = RequestWrapper()

    # start test cases
    def test_001_get_all_products(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.PRODUCTS_URL)
        assert response.status_code == 200

    def test_002_get_single_product(self):
        product_id = "1"
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.PRODUCTS_URL + "/" + product_id)
        assert response.status_code == 200
        assert "Fjallraven" in response.json()["title"]

    def test_003_add_single_product(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.POST,
                                                  url=self.testdata.PRODUCTS_URL,
                                                  json=self.testdata.SINGLE_PRODUCT_PAYLOAD)

        assert response.status_code == 200
        assert "Shailbi" in response.json()["title"]

    def test_004_limit_and_sort_products(self):
        limit = 8
        param = {"limit": limit, "sort": "asc"}
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.PRODUCTS_URL,
                                                  params=param)
        assert response.status_code == 200
        for i in range(0, limit):
            assert i+1 == response.json()[i]["id"]

    def test_005_products_categories(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.CATEGORIES_URL)
        assert response.status_code == 200
        assert response.json() == self.response_data.PRODUCT_CATEGORIES_RESPONSE

    def test_006_get_products_specific_categories(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.SPECIFIC_CATEGORY_URL )
        assert response.status_code == 200
        assert response.json() == self.response_data.SPECIFIC_PRODUCT_CATEGORY_RESPONSE

    def test_006_update_product(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.PUT,
                                                  url=self.testdata.PRODUCTS_URL + "/7",
                                                  json=self.payload_data.UPDATE_PRODUCT_DETAILS)
        assert response.status_code == 200
        assert response.json() == self.response_data.UPDATED_PRODUCT_RESPONSE

    def test_007_partial_update_product(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.PATCH,
                                                  url=self.testdata.PRODUCTS_URL + "/7",
                                                  json=self.payload_data.PARTIAL_UPDATE_PRODUCT_DETAILS)
        assert response.status_code == 200
        assert response.json() == self.response_data.PARTIAL_UPDATED_PRODUCT_RESPONSE

    def test_008_delete_product(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.DELETE,
                                                  url=self.testdata.PRODUCTS_URL + "/6")
        assert response.status_code == 200
        # json_obj = json.load(open("src/constrants/products_response.json", "r+"))
        # print(json_obj)

