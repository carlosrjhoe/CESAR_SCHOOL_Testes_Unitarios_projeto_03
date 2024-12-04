from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            result = "No momento temos os seguintes sabores:"
            for flavor in self.flavors:
                result += f" {flavor}"
            return result
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível.

        Erros identificados:
            Mensagens confusas e um pouco específicas para o sabor pesquisado.
            Retorno consumista de uma lista completa
            ( self.flavors) em vez do sabor pesquisado.
            Redundância na lógica condicional ao verificar
            duas vezes se existe uma lista de sabores.

        Pontos de melhoria:
            Ajustar as mensagens para serem mais específicas e naturais,
            mencionando diretamente o sabor pesquisado.
            Separar a lógica de construção de mensagens em
            condições mais claras e enxutas.
            Reduzir redundâncias ao verificar diretamente a
            presença do sabor com in."""

        if not self.flavors:
            return "Estamos sem estoque atualmente!"
        if flavor in self.flavors:
            return f"Temos no momento o sabor {flavor}!"
        return f"Não temos no momento o sabor {flavor}!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                return "\nSabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Estamos sem estoque atualmente!"
