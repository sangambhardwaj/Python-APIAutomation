from fake_stone_api.src.constrants.api_testdata import APITestData
from fake_stone_api.src.helpers.api_request_wrapper import RequestWrapper
from fake_stone_api.src.constrants.payload_data import ApiPayloadData

class TestFakeStoreLoginAPIs:
    payload_data = ApiPayloadData()
    testdata = APITestData()
    request_wrapper = RequestWrapper()


    def test_login(self):
        response = self.request_wrapper.requester(method=self.testdata.HTTP.POST,
                                                  url=self.testdata.LOGIN_URL,
                                                  json=self.payload_data.LOGIN_DETAILS)
        assert response.status_code == 200
        # assert response.json() == self.response_data.TOKEN

