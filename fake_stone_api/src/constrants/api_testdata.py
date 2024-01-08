# Add your constants here
import json

from dotted_dict import DottedDict


class APITestData:
    # Valid HTTP methods
    HTTP = DottedDict({
        "GET": "get",
        "POST": "post",
        "PUT": "put",
        "PATCH": "patch",
        "DELETE": "delete"
    })

    # URLs

    # PRODUCT URLs
    BASE_URL = "https://fakestoreapi.com"
    PRODUCT_URL = BASE_URL + "/product"
    PRODUCTS_URL = BASE_URL + "/products"
    CATEGORIES_URL = PRODUCTS_URL + "/categories"
    SPECIFIC_CATEGORY_URL = PRODUCTS_URL + "/category/jewelery"

    # LOGIN URL
    LOGIN_URL = BASE_URL + "/auth/login"

    # USERS URLs
    USERs_URL = BASE_URL + "/users"
    USER_URL = USERs_URL + "/1"

    # CART URLs
    CARTs_URL = BASE_URL + "/carts"
    CART_BASE_URL = CARTs_URL + "/5"
    CART_GET_USER_URL = CARTs_URL + "/user/2"

    # API Test Data
    SINGLE_PRODUCT_PAYLOAD = {
        "title": "test product by Shailbi",
        "price": 133.5,
        "description": "lorem ipsum set my desc",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }

    json_obj = json.load(open("src/constrants/cart_response.json", "r+"))
    # json_obj = DottedDict(json_obj)
    json_all_users = json.load(open("src/constrants/users_response.json", "r+"))
