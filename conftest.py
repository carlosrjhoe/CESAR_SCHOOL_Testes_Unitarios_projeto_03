from pytest import fixture
from src.models.restaurant import Restaurant


@fixture
def setUp():
    restaurant_name = "Bolos da May"
    cuisine_type = "Bolos tipicos"
    return Restaurant(restaurant_name, cuisine_type)
