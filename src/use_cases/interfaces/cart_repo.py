# ===== src/use_cases/interfaces/cart_repo.py =====
from abc import ABC, abstractmethod
from src.entities.cart import Cart


class CartRepository(ABC):
    @abstractmethod
    def find_by_cliente(self, id_cliente: int) -> Cart | None:
        ...

    @abstractmethod
    def save(self, cart: Cart) -> None:
        ...