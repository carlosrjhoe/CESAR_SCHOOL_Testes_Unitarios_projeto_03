import pytest


class TestIceCreamStand:

    @pytest.mark.parametrize(
        "sabores, esperado",
        [
            (
                ["macaxeira", "fubá"],
                "No momento temos os seguintes sabores: macaxeira fubá",
            ),
            ([], "Estamos sem estoque atualmente!"),
            (["chocolate"], "No momento temos os seguintes sabores: chocolate")
        ],
    )
    def test_flavors_available(self, setup_ice_cream, sabores, esperado):
        object_flavors = setup_ice_cream
        object_flavors.flavors = sabores
        resultado = object_flavors.flavors_available()
        assert resultado == esperado

    @pytest.mark.parametrize(
        "sabores, sabor_para_verificar, esperado",
        [
            (
                ["chocolate", "baunilha", "morango"],
                "chocolate",
                "Temos no momento o sabor chocolate!",
            ),
            (
                ["chocolate", "baunilha", "morango"],
                "limão",
                "Não temos no momento o sabor limão!",
            ),
            ([], "chocolate", "Estamos sem estoque atualmente!"),
            (None, "baunilha", "Estamos sem estoque atualmente!"),
        ],
    )
    def test_find_flavor(
        self, setup_ice_cream, sabores, sabor_para_verificar, esperado
    ):
        object_flavors = setup_ice_cream
        object_flavors.flavors = sabores
        resultado = object_flavors.find_flavor(sabor_para_verificar)
        assert resultado == esperado

    @pytest.mark.parametrize(
        "sabores, sabor_para_verificar, esperado",
        [
            (
                ["chocolate", "baunilha"],
                "morango",
                "morango adicionado ao estoque!",
            ),
            (
                ["chocolate", "baunilha"],
                "chocolate",
                "\nSabor já disponível!",
            ),
            ([], "morango", "morango adicionado ao estoque!"),
            (None, "morango", "morango adicionado ao estoque!"),
        ],
    )
    def test_add_flavor(
        self, setup_ice_cream, sabores, sabor_para_verificar, esperado
    ):
        object_flavors = setup_ice_cream
        object_flavors.flavors = sabores
        resultado = object_flavors.add_flavor(sabor_para_verificar)
        assert resultado == esperado
