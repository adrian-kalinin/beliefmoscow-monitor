import requests
import math

import settings


def _extract_useful_data(product):
    data = {
        'id': product['id'],
        'title': product['title'],
        'link': settings.BASE_URL + product['url'],
        'sizes': []
    }

    for variant in product['variants']:
        data['sizes'].append({
            'title': variant['title'],
            'quantity': variant['quantity'],
            'price': variant['price']
        })

    return data


def get_number_of_pages():
    current_path = settings.COLLECTION_PATH.format(page_size=settings.PAGE_SIZE, page=1)
    response = requests.get(settings.BASE_URL + current_path)

    if response.status_code == 200:
        data = response.json()

        return math.ceil(data['count'] / settings.PAGE_SIZE)


def retrieve_products():
    if number_of_pages := get_number_of_pages():
        products = []

        for page in range(number_of_pages):
            current_path = settings.COLLECTION_PATH.format(page_size=settings.PAGE_SIZE, page=page+1)
            response = requests.get(settings.BASE_URL + current_path)

            if response.status_code == 200:
                data = response.json()
                products.extend(data['products'])

        return products


def search_keywords(products):
    target_products = []

    for product in products:
        for keyword in settings.KEYWORDS:
            if keyword in product['title'].lower():
                product_data = _extract_useful_data(product)
                target_products.append(product_data)

    return target_products
