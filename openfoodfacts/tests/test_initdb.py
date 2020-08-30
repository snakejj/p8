import pytest
from mixer.backend.django import mixer
from openfoodfacts.management.commands.initdb import Command
pytestmark = pytest.mark.django_db


def test_initdb_command_is_fetching_data_from_the_openfoodfacts_api(monkeypatch):
    obj_test = mixer.blend('products.Product')
    obj_test2 = mixer.blend('products.Product')
    obj_test3 = mixer.blend('products.Product')

    class MockGet:
        def __init__(self, url, params):
            pass

        def json(self):

            return {
                "products": [
                    {
                        "code": obj_test.code,
                        "product_name_fr": obj_test.product_name,
                        "url": obj_test.product_url,
                        "nutrition_grade_fr": obj_test.nutrition_grade_fr,
                        "image_url": obj_test.image_url,
                        "image_nutrition_url": obj_test.image_nutrition_url,
                    },
                    {
                        "code": obj_test2.code,
                        "product_name_fr": obj_test2.product_name,
                        "url": obj_test2.product_url,
                        "nutrition_grade_fr": obj_test2.nutrition_grade_fr,
                        "image_url": obj_test2.image_url,
                        "image_nutrition_url": obj_test2.image_nutrition_url,
                    },
                    {
                        "code": obj_test3.code,
                        "product_name_fr": obj_test3.product_name,
                        "url": obj_test3.product_url,
                        "nutrition_grade_fr": obj_test3.nutrition_grade_fr,
                        "image_url": obj_test3.image_url,
                        "image_nutrition_url": obj_test3.image_nutrition_url,
                    }
                ]
            }

    monkeypatch.setattr("requests.get", MockGet)

    cmd_instance = Command()
    assert str(obj_test.code) and str(obj_test2.code) and str(obj_test3.code) in str(cmd_instance.handle()), ''
