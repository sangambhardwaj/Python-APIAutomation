# from src.constants.api_constants import BASE_URL, APIConstants, base_url
import pytest

from booking.src.constants.api_constants import APIConstants
from booking.src.helpers.api_requests_wrapper import post_requests
from booking.src.helpers.common_verification import verify_http_status_code
from booking.src.helpers.utils import common_headers_json


class TestCreateBooking(object):

    @pytest.mark.positive
    def test_create_booking_tc1(self):
        # URL, Headers, Payload,
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload={}, in_json=False)
        verify_http_status_code(response, 500)

    @pytest.mark.positive
    def test_create_booking_tc2(self):
        # URL, Headers, Payload,
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload={"firstname": "admin"}, in_json=False)
        verify_http_status_code(response, 500)

    def test_create_booking_tc3(self):
        # URL, Headers, Payload,
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=None, in_json=False)
        verify_http_status_code(response, 400)

    def test_create_booking_tc4(self):
        # URL, Headers, Payload,
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload="This is Text", in_json=False)
        verify_http_status_code(response, 400)
