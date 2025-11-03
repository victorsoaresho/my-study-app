from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    """Modelo de dados para um Produto."""
    id: int
    name: str
    price: float
    quantity: int