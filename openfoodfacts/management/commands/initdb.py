import json

from django.core.management.base import BaseCommand, CommandError
import requests
import sys

from products.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        """Part which make the api request, put all the data in a
        variable"""

        categories = [
            'fr:Pâtes à tartiner',
            'Yaourts',
            'Chocolats',
            'Boissons',
            'Snacks',
            'Produits laitiers'
        ]

        products = {} # rename datasomething

        for categ in categories:

            url = "https://fr.openfoodfacts.org/cgi/search.pl"

            data = {
                "action": "process",
                "json": 1,
                "page_size": 1000,
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": categ,
                "sort_by" : "unique_scans_n",
            }
            response = requests.get(url, params=data)
            products[categ] = response.json()['products']

        """Part which erase data lacking information within the variable results """

        clean_result = {}

        for categ in products:

            clean_result[categ] = []

            try:
                for p in products[categ]:
                    if (p.get('code', "")
                        and len(p.get('nutrition_grade_fr', "")) == 1
                        and 4 < len(p.get('product_name_fr', "")) < 80
                        and 1 < len(p.get('url', "")) < 255
                        and 1 < len(p.get('image_url', "")) < 255
                        and 1 < len(p.get('image_nutrition_url', "")) < 255
                    ):

                        fullp = {
                            "code": p['code'],
                            "product_name": p["product_name_fr"],
                            "product_url": p["url"],
                            "nutrition_grade_fr": p["nutrition_grade_fr"],
                            "image_url": p["image_url"],
                            "image_nutrition_url": p["image_nutrition_url"],
                        }

                        clean_result[categ].append(fullp)

            except KeyError:
                self.stderr.write("Erreur lors du tri", ending='')

        # Save data in database

        Product.objects.create_products_from_openfoodfacts(clean_result)

        return json.dumps(clean_result, indent=2)
