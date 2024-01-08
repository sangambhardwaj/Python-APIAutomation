import requests


class Test_API():
    # test case variable

    token = None
    my_json = None
    my_url = "https://reqres.in/api/"
    post_payload = {
        "name": "morpheus",
        "job": "leader"
    }
    new_registration = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    user_update = {
        "name": "morpheus",
        "job": "zion resident"
    }

    # start test cases
    def test_001_get_single_user_response(self):
        response = requests.get(url=self.my_url + "users/2")

        assert response.status_code == 200

        print("response.json", response.json())

    def test_002_get_all_user_response(self):
        response = requests.get(url=self.my_url + "users?page=2")

        assert response.status_code == 200
        assert response.json()["data"]["id"] == 7
        print("response.json", response.json())

    def test_003_post_user_responce(self):
        response = requests.post(url=self.my_url + "users", data=self.post_payload)

        assert response.status_code == 201
        print("response.json", response.json())

    def test_004_post_user_register_responce(self):
        response = requests.post(url=self.my_url + "register", data=self.registered_payload)

        assert response.status_code == 200
        print("response.json", response.json())

    def test_005_put_user_responce(self):
        response = requests.put(url=self.my_url + "users/2", data=self.put_payload)

        assert response.status_code == 200
        assert response.json()['name'] == 'morpheus'
        print("response.json", response.json())
