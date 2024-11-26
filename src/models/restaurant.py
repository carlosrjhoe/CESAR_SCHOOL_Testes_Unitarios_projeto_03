class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante

        Erros identificados:
            Erros de digitação, Mensagem confusa, Uso de variáveis

        Pontos de melhoria:
            Separar a lógica de construção do texto em métodos auxiliares
            ou variáveis ​​para maior clareza e modularidade.
            Evitar redundâncias e construa frases mais
            naturais em português
        """

        return f"Este restaurante se chama {self.restaurant_name}"

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o
        restaurante está aberto para negócios."""
        if not self.open:
            self.open = True
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está
        fechado para negócios."""
        if self.open:
            self.open = True
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este
        restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served = more_customers
        else:
            return f"{self.restaurant_name} está fechado!"
