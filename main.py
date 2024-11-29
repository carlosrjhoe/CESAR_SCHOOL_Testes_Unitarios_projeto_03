from src.models.restaurant import Restaurant

testrestaurante = Restaurant("Bolos da May", "Bolos tipicos")
print(testrestaurante.close_restaurant())
# print(testrestaurante.open_restaurant())
# print(testrestaurante.increment_number_served(5))
print(testrestaurante.increment_number_served(50))
# print(testrestaurante.increment_number_served(-10))
print(testrestaurante.describe_restaurant())
