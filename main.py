import logging
import time

import scraper
import models
import settings


logging.basicConfig(
    format='%(asctime)s – %(levelname)s – %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)


def configure_database():
    models.database.connect()
    models.database.create_tables([models.Product])
    models.database.close()
    logging.info('Database has been configured')


def retrieve_new_products():
    logging.info('Searching for new products')

    products = scraper.retrieve_products()
    target_products = scraper.search_keywords(products)

    new_products = []

    for product in target_products:
        _, created = models.Product.get_or_create(product_id=product['id'])

        if created:
            new_products.append(product)

    return new_products


def main():
    configure_database()

    while True:
        if new_products := retrieve_new_products():
            logging.info(f'Found {len(new_products)} new products')

            for product in new_products:
                print(product)

        time.sleep(settings.DELAY)


if __name__ == '__main__':
    main()
