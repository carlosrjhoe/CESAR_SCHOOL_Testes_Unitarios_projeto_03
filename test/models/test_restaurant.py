import pytest


class TestRestaurant:

    def test_describe_restaurant(self, setup):
        """Testa a descrição do restaurante"""
        object_restaurant = setup
        resultado = object_restaurant.describe_restaurant()
        esperado = "Este restaurante se chama Bolos Da May"
        assert resultado == esperado

    @pytest.mark.parametrize(
        "estado_inicial, esperado",
        [
            (False, "Bolos Da May agora está aberto!"),
            (True, "Bolos Da May já está aberto!"),
        ],
    )
    def test_open_restaurant(self, setup, estado_inicial, esperado):
        """Testa restaurante está aberto para negócios."""
        object_restaurant = setup
        object_restaurant.open = estado_inicial
        resultado = object_restaurant.open_restaurant()
        assert resultado == esperado

    @pytest.mark.parametrize(
        "estado_inicial, esperado",
        [
            (True, "Bolos Da May agora está fechado!"),
            (False, "Bolos Da May já está fechado."),
        ],
    )
    def test_close_restaurant(self, setup, estado_inicial, esperado):
        """Testa restaurante está fechado para negócios."""
        object_restaurant = setup
        object_restaurant.open = estado_inicial
        resultado = object_restaurant.close_restaurant()
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
        self, setup, estado_inicial, total_customers, msg_esperada
    ):
        object_restaurant = setup
        object_restaurant.open = estado_inicial
        resultado = object_restaurant.set_number_served(total_customers)
        assert resultado == msg_esperada

    @pytest.mark.parametrize(
        "estado_inicial, more_customers, msg_esperada",
        [
            (True, 50, "Total de 50 clientes atendidos!"),
            (True, -10, "O número de clientes não pode ser negativo!"),
            (False, 0, "O restaurante Bolos Da May está fechado!"),
        ],
    )
    def test_increment_number_served(
        self, setup, estado_inicial, more_customers, msg_esperada
    ):
        object_restaurant = setup
        object_restaurant.open = estado_inicial
        resultado = object_restaurant.increment_number_served(more_customers)
        assert resultado == msg_esperada
