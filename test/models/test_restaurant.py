class TestRestaurant:

    def test_describe_restaurant(self, setUp):
        """Testa a descrição do restaurante"""
        restaurantTest = setUp
        resultado = restaurantTest.describe_restaurant()
        esperado = ("Este restaurante se chama Bolos Da May")
        assert resultado == esperado

    # def test_open_restaurant(self):
    #     assert False

    # def test_close_restaurant(self):
    #     assert False

    # def test_set_number_served(self):
    #     assert False

    # def test_increment_number_served(self):
    #     assert False
