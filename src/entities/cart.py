# ===== src/entities/cart.py =====
from dataclasses import dataclass, field
import uuid
from src.entities.currency import Currency


@dataclass
class CartItem:
    id_product: uuid.UUID
    product_name: str
    price: float
    currency: Currency
    quantity: int

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")


@dataclass
class Cart:
    id_cliente: int
    items: list[CartItem] = field(default_factory=list)

    def add_item(self, id_product: uuid.UUID, product_name: str, price: float, currency: Currency, quantity: int) -> None:
        for item in self.items:
            if item.id_product == id_product:
                item.quantity += quantity
                return
        self.items.append(CartItem(
            id_product=id_product,
            product_name=product_name,
            price=price,
            currency=currency,
            quantity=quantity,
        ))

    def total_by_currency(self) -> dict[str, float]:
        """Calcule le total, regroupé par devise (car dollar/gourde/euro ne se mélangent pas)."""
        totals: dict[str, float] = {}
        for item in self.items:
            key = item.currency.value
            totals[key] = totals.get(key, 0) + (item.price * item.quantity)
        return totals