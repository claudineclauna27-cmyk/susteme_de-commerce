# ===== src/entities/product.py =====
from dataclasses import dataclass, field
from typing import Optional
import uuid
from src.entities.currency import Currency


@dataclass
class Product:
    product_name: str
    price: float
    quantity: int
    currency: Currency
    photo_url: Optional[str] = None
    id_product: uuid.UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        if not self.product_name or not self.product_name.strip():
            raise ValueError("please enter the name")
        if self.price < 0:
            raise ValueError("price can't be negative")
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")