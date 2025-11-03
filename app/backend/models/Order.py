from dataclasses import dataclass

from models.Product import Product
from models.OrderState import OrderState

@dataclass
class Order:
    """
    Representa um Pedido (Ordem de Compra) com lógica de negócio.
    """
    order_id: int
    customer_id: int
    state: OrderState = OrderState.PENDING
    
    @property
    def total_amount(self) -> float:
        """Calcula e retorna o valor total do pedido."""
        return sum(product.price * product.quantity for product in self.products)

    def add_product(self, product: Product):
        """Adiciona um produto ao pedido."""
        
        if any(p.id == product.id for p in self.products):
            raise ValueError(f"Produto (ID: {product.id}) já existe no pedido.")
        
        self.products.append(product)
        
    def remove_product(self, product: Product):
        """Remove um produto do pedido."""
        try:
            self.products.remove(product)
        except ValueError:
            raise ValueError(f"Produto (ID: {product.id}) não encontrado no pedido.")

    def update_state(self, new_state: OrderState):
        """Atualiza o estado do pedido, com validação."""
        
        if not isinstance(new_state, OrderState):
            raise TypeError("Estado fornecido não é um OrderState válido.")
        
        print(f"Pedido {self.order_id}: Estado mudou de {self.state.name} para {new_state.name}")
        self.state = new_state
