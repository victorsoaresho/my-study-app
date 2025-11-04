from models.Order import Order
from models.OrderState import OrderState
from models.Product import Product

class OrderService:
    """
    Controlador (Camada de Serviço) para gerenciar a lógica de 
    negócio de múltiplos pedidos.
    """
    def __init__(self):
        self._orders: dict[int, Order] = {}
        self._next_order_id: int = 1

    def create_order(self, customer_id: int) -> Order:
        """ Cria um novo pedido para um cliente. """
        new_order = Order(
            order_id=self._next_order_id,
            customer_id=customer_id
        )
        self._orders[new_order.order_id] = new_order
        self._next_order_id += 1
        print(f"Novo pedido criado: ID {new_order.order_id} para Cliente {customer_id}")
        return new_order

    def get_order(self, order_id: int) -> Order:
        """ Busca um pedido pelo seu ID. """
        order = self._orders.get(order_id)
        if not order:
            raise ValueError(f"Pedido com ID {order_id} não encontrado.")
        return order

    def add_product_to_order(self, order_id: int, product: Product) -> Order:
        """ Controla a ação de adicionar um produto a um pedido. """
        order = self.get_order(order_id)
        try:
            order.add_product(product)
            return order
        except ValueError as e:
            print(f"Erro: {e}")
            raise

    def change_order_state(self, order_id: int, new_state_name: str) -> Order:
        """ Controla a ação de mudar o estado de um pedido. """
        try:
            new_state = OrderState[new_state_name.upper()]
        except KeyError:
            raise ValueError(f"'{new_state_name}' não é um estado válido.")

        order = self.get_order(order_id)
        order.update_state(new_state)
        return order