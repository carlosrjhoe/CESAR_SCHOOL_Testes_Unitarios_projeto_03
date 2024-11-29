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

    @pytest.mark.parametrize(
        "estado_inicial, esperado",
        [
            (True, "Bolos Da May agora está fechado!"),
            (False, "Bolos Da May já está fechado."),
        ],
    )
    def test_close_restaurant(self, setUp, estado_inicial, esperado):
        """Testa restaurante está fechado para negócios."""
        restaurantTest = setUp
        restaurantTest.open = estado_inicial
        resultado = restaurantTest.close_restaurant()
        assert resultado == esperado

    @pytest.mark.parametrize(
        "estado_inicial, total_customers, msg_esperada",
        [
            (True, 50, "O restaurante Bolos Da May já atendeu 50 clientes."),
            (True, -10, "O número de clientes deve ser um inteiro positivo."),
            (True, "um", "O número de clientes deve ser um inteiro positivo."),
            (False, 50, "Bolos Da May está fechado!"),
        ],
    )
    def test_set_number_served(
        self, setUp, estado_inicial, total_customers, msg_esperada
    ):
        restaurantTest = setUp
        restaurantTest.open = estado_inicial
        resultado = restaurantTest.set_number_served(total_customers)
        assert resultado == msg_esperada

    # def test_increment_number_served(self):
    #     assert False
