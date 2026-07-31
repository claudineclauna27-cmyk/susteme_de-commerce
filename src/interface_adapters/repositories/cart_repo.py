# ===== src/interface_adapters/repositories/cart_repo.py =====
from src.use_cases.interfaces.cart_repo import CartRepository
from src.entities.cart import Cart


class CartRepositoryImpl(CartRepository):
    def __init__(self, db):
        self.db = db

    def find_by_cliente(self, id_cliente: int) -> Cart | None:
        return self.db.find_by_cliente(id_cliente)

    def save(self, cart: Cart) -> None:
        self.db.save(cart)