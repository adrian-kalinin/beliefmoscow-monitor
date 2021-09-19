import scraper


def main():
    products = scraper.retrieve_products()
    target_products = scraper.search_keywords(products)

    for product in target_products:
        print(product)


if __name__ == '__main__':
    main()
