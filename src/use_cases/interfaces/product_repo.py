# ===== src/usecase/interfaces/product_repository.py =====
from abc import ABC, abstractmethod
from src.entities.product import Product
import uuid


class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product) -> None:
        ...

    @abstractmethod
    def find_by_id(self, id_product: uuid.UUID) -> Product | None:
        ...

    @abstractmethod
    def list_all(self) -> list[Product]:
        ...