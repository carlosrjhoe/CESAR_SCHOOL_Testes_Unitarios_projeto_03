from pytest import fixture
from src.models.restaurant import Restaurant
from src.models.ice_cream_stand import IceCreamStand


@fixture
def setup():
    restaurant_name = "Bolos da May"
    cuisine_type = "Bolos tipicos"
    return Restaurant(restaurant_name, cuisine_type)


@fixture
def setup_ice_cream():
    restaurant_name = "Bolos da May"
    cuisine_type = "Bolos tipicos"
    flavors = ["macaxeira", "fubá"]
    return IceCreamStand(restaurant_name, cuisine_type, flavors)
