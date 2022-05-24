#representer uma entidade no banco de dados

class Produto:
    def __init__(self, description, price, quantity, id):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity