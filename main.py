from src.models.restaurant import Restaurant

testrestaurante = Restaurant("Bolos da May", "Bolos tipicos")
print(testrestaurante.open_restaurant())
print(testrestaurante.close_restaurant())
print(testrestaurante.describe_restaurant())