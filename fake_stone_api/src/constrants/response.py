class ApiResponse:
    # login token
    TOKEN = {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjIsInVzZXIiOiJtb3JfMjMxNCIsImlhdCI6MTcwNDYwNjY5OX0.Ni_WmX4bEm_bpIE9LfggAhoSIBvsTv2S_fbv82C75W4"}

    # PRODUCT RESPONSE
    PARTIAL_UPDATED_PRODUCT_RESPONSE = {
        "id": 7,
        "title": "Ring",
        "price": 1.2,
        "image": "https://i.pravatar.cc",
        "category": "jewelery"
    }

    NEW_PRODUCT_RESPONSE = {
        "id": 21,
        "title": "computer",
        "price": 13.5,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }

    UPDATED_PRODUCT_RESPONSE = {
        "id": 7,
        "title": "i_Phone",
        "price": 1.2,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }

    PRODUCT_CATEGORIES_RESPONSE = [
        "electronics",
        "jewelery",
        "men's clothing",
        "women's clothing"
    ]

    SPECIFIC_PRODUCT_CATEGORY_RESPONSE = [
        {
            "id": 5,
            "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
            "price": 695,
            "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
            "category": "jewelery",
            "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg",
            "rating": {
                "rate": 4.6,
                "count": 400
            }
        },
        {
            "id": 6,
            "title": "Solid Gold Petite Micropave ",
            "price": 168,
            "description": "Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.",
            "category": "jewelery",
            "image": "https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg",
            "rating": {
                "rate": 3.9,
                "count": 70
            }
        },
        {
            "id": 7,
            "title": "White Gold Plated Princess",
            "price": 9.99,
            "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...",
            "category": "jewelery",
            "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg",
            "rating": {
                "rate": 3,
                "count": 400
            }
        },
        {
            "id": 8,
            "title": "Pierced Owl Rose Gold Plated Stainless Steel Double",
            "price": 10.99,
            "description": "Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel",
            "category": "jewelery",
            "image": "https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg",
            "rating": {
                "rate": 1.9,
                "count": 100
            }
        }
    ]

    # USER RESPONSE

    NEW_USER_RESPONSE = {
        "id": 1
    }

    UPDATED_USER_RESPONSE = {
        "email": "John@gmail.com",
        "username": "Sangam",
        "password": "m38rmF$",
        "name": [
            {
                "firstname": "John",
                "lastname": "Doe"
            }
        ],
        "address": {
            "city": "kilcoole",
            "street": "7835 new road",
            "number": 3,
            "zipcode": "12926-3874"
        },
        "geolocation": {
            "lat": "-37.3159",
            "long": "81.1496"
        },
        "phone": "1-570-236-7033"
    }

    PARTIAL_UPDATED_USER_RESPONSE = {
        "email": "sangam@gmail.com",
        "username": "Sangam bhardwaj"
    }

    ADD_CART_NEW_PRODUCT_RESPONSE = {
        "id": 11,
        "userId": 5,
        "date": "2020-02-03",
        "products": [
            {
                "productId": 5,
                "quantity": 3
            },
            {
                "productId": 1,
                "quantity": 5
            }
        ]
    }

    UPDATED_CART_PRODUCT_RESPONSE = {
        "id": 7,
        "userId": 6,
        "date": "2020-05-03",
        "products": [
            {
                "productId": 6,
                "quantity": 3
            },
            {
                "productId": 1,
                "quantity": 5
            }
        ]
    }

    PARTIAL_UPDATED_CART_PRODUCT_RESPONSE = {
        "id": 7,
        "userId": 12,
        "date": "2021-05-03",
        "products": [
            {
                "productId": 6,
                "quantity": 3
            }
        ]
    }
