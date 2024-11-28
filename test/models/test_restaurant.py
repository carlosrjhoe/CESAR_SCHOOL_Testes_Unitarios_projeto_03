import pytest


class TestRestaurant:

    def test_describe_restaurant(self, setUp):
        """Testa a descrição do restaurante"""
        restaurantTest = setUp
        resultado = restaurantTest.describe_restaurant()
        esperado = "Este restaurante se chama Bolos Da May"
        assert resultado == esperado

    @pytest.mark.parametrize(
        "estado_inicial, esperado",
        [
            (False, "Bolos Da May agora está aberto!"),
            (True, "Bolos Da May já está aberto!"),
        ],
    )
    def test_open_restaurant(self, setUp, estado_inicial, esperado):
        """Testa restaurante está aberto para negócios."""
        restaurantTest = setUp
        restaurantTest.open = estado_inicial
        resultado = restaurantTest.open_restaurant()
        assert resultado == esperado

    def test_close_restaurant(self, setUp):
        """Testa restaurante está fechado para negócios."""
        restaurantTest = setUp
        resultado = restaurantTest.close_restaurant()
        esperado = "Bolos Da May já está fechado."
        assert resultado == esperado

    # def test_set_number_served(self):
    #     assert False

    # def test_increment_number_served(self):
    #     assert False
