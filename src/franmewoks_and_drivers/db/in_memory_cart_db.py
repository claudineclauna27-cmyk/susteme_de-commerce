# ===== src/franmewoks_and_drivers/db/in_memory_cart_db.py =====
from src.entities.cart import Cart


class InMemoryCartDB:
    def __init__(self):
        self.data: dict[int, Cart] = {}

    def find_by_cliente(self, id_cliente: int) -> Cart | None:
        return self.data.get(id_cliente)

    def save(self, cart: Cart) -> None:
        self.data[cart.id_cliente] = cart