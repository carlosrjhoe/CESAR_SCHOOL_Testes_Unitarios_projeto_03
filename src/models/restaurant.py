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
        restaurante está aberto para negócios.

        Erros identificados:
            Erro de digitação na docstring, Mensagem Retornada,
            Lógica Repetitiva, Tipo de Retorno Não Especificado,
            Responsabilidade Única.

        Pontos de melhoria:
            Padronização das Mensagens, Melhoria da Docstring.
        """
        if not self.open:
            self.open = True
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está
        fechado para negócios.

        Erros identificados:
            Lógica incorreta ao fechar o restaurante
            (`self.open` é redefinido como `True` em vez de `False`).
            Reseta `self.number_served` sem necessidade.

        Pontos de melhoria:
            Corrigir a lógica para alterar o estado
            do restaurante adequadamente.
            Melhorar a docstring para refletir as mudanças."""
        if self.open:
            self.open = False
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado."

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este
        restaurante até o momento.

        Erros identificados:
            Sem validação para `total_customers` ser um número positivo.
            A lógica não impede valores negativos ou inválidos.
            Retorno inconsistente quando o restaurante está fechado.

        Pontos de melhoria:
            Validar que `total_customers` seja um inteiro positivo.
            Melhorar a mensagem de erro para refletir
            adequadamente o problema."""
        if not isinstance(total_customers, int) or total_customers < 0:
            return "O número de clientes deve ser um inteiro positivo."
        if self.open:
            self.number_served = total_customers
            return (
                f"O restaurante {self.restaurant_name} "
                f"já atendeu {self.number_served} clientes."
            )
        return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served = more_customers
        else:
            return f"{self.restaurant_name} está fechado!"
