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
            (["chocolate"], "No momento temos os seguintes sabores: chocolate"),
        ],
    )
    def test_flavors_available(self, setUp_ice_cream, sabores, esperado):
        object_flavors = setUp_ice_cream
        object_flavors.flavors = sabores
        resultado = object_flavors.flavors_available()
        assert resultado == esperado


#     def test_find_flavor(self):
#         assert False

#     def test_add_flavor(self):
#         assert False
