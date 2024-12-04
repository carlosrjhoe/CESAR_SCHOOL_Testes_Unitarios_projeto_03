from src.models.restaurant import Restaurant
from src.models.ice_cream_stand import IceCreamStand

testrestaurante = Restaurant("Bolos da May", "Bolos tipicos")
# print(testrestaurante.close_restaurant())
# # print(testrestaurante.open_restaurant())
# # print(testrestaurante.increment_number_served(5))
# print(testrestaurante.increment_number_served(50))
# # print(testrestaurante.increment_number_served(-10))
# print(testrestaurante.describe_restaurant())

test_acecream = IceCreamStand("Bolos da May", "Bolos tipicos",
                              ["macaxeira", "fubá"])
# print(test_acecream.flavors_available())
print(test_acecream.find_flavor("fubá"))
# print(test_acecream.find_flavor("pé de moleque"))
