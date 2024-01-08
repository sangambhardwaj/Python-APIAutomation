# Login payload
class ApiPayloadData:
    LOGIN_DETAILS = {
        "username": "mor_2314",
        "password": "83r5^_"
    }

    # USER PAYLOAD
    NEW_USER_DETAILS = {
        "email": "John@gmail.com",
        "username": "John",
        "password": "m38rmF$",
        "name": [{
            "firstname": "John",
            "lastname": "Doe"}],
        "address": {
            "city": "kilcoole",
            "street": "7835 new road",
            "number": 3,
            "zipcode": "12926-3874"},
        "geolocation": {
            "lat": "-37.3159",
            "long": "81.1496"
        },
        "phone": "1-570-236-7033"
    }

    UPDATE_USER_DETAILS = {
        "email": "John@gmail.com",
        "username": "Sangam",
        "password": "m38rmF$",
        "name": [{
            "firstname": "John",
            "lastname": "Doe"}],
        "address": {
            "city": "kilcoole",
            "street": "7835 new road",
            "number": 3,
            "zipcode": "12926-3874"},
        "geolocation": {
            "lat": "-37.3159",
            "long": "81.1496"
        },
        "phone": "1-570-236-7033"
    }

    PARTIAL_UPDATE_USER_DETAILS = {
        "email": "sangam@gmail.com",
        "username": "Sangam bhardwaj"
    }

    # CART PAYLOAD
    POST_PAYLOAD = {
        "userId": 5,
        "date": "2020-02-03",
        "products": [{"productId": 5, "quantity": 3}, {"productId": 1, "quantity": 5}]
    }

    UPDATE_CART_DETAILS = {
        "userId": 6,
        "date": "2020-05-03",
        "products": [{"productId": 6, "quantity": 3}, {"productId": 1, "quantity": 5}]
    }

    PARTIAL_UPDATE_CART_DETAILS = {
        "userId": 12,
        "date": "2021-05-03",
        "products": [{"productId": 6, "quantity": 3}]
    }

    # PRODUCT PAYLOAD

    ADD_NEW_PRODUCT = {
        "title": "computer",
        "price": 13.5,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }

    UPDATE_PRODUCT_DETAILS = {
        "title": "i_Phone",
        "price": 1.20,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }

    PARTIAL_UPDATE_PRODUCT_DETAILS = {
        "title": "Ring",
        "price": 1.20,
        "image": "https://i.pravatar.cc",
        "category": "jewelery"
    }
