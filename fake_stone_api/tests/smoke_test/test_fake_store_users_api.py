from fake_stone_api.src.constrants.api_testdata import APITestData
from fake_stone_api.src.helpers.api_request_wrapper import RequestWrapper
from fake_stone_api.src.constrants.response import ApiResponse
from fake_stone_api.src.constrants.payload_data import ApiPayloadData
from fake_stone_api.src.constrants.params import Param


class TestFakeStoreUserAPIs:

    param = Param()
    payload_data = ApiPayloadData()
    response_data = ApiResponse()
    testdata = APITestData()
    request_wrapper = RequestWrapper()


    def test_001_get_all_user_details(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.USERs_URL)
        assert response.status_code == 200
        assert response.json() == self.testdata.json_all_users

    def test_002_get_single_user(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.USER_URL)
        assert response.status_code == 200
        assert response.json() == self.testdata.json_all_users[0]

    def test_003_limit_user(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.GET,
                                                  url=self.testdata.USERs_URL,
                                                  params=self.param.user_param)
        assert response.status_code == 200
        # assert response.json()[2] == {"a":1, "b":2}

    def test_004_add_user(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.POST,
                                                  url=self.testdata.USERs_URL,
                                                  json=self.payload_data.NEW_USER_DETAILS)
        assert response.status_code == 200
        assert response.json()["id"] in [11,1]

    def test_005_update_user_details(self):
        user_id = "7"
        response = self.request_wrapper.requester(method=self.testdata.HTTP.PUT,
                                                  url=self.testdata.USERs_URL + "/" + user_id,
                                                  json=self.payload_data.UPDATE_USER_DETAILS)
        assert response.status_code == 200
        assert response.json() == self.response_data.UPDATED_USER_RESPONSE

    def test_007_partial_update_in_user(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.PATCH,
                                                  url=self.testdata.USERs_URL + "/7",
                                                  json=self.payload_data.PARTIAL_UPDATE_USER_DETAILS)
        assert response.status_code == 200
        assert response.json() == self.response_data.PARTIAL_UPDATED_USER_RESPONSE




       # " python -m pytest .\tests\smoke_test\test_fake_store_users_api.py -s -v"