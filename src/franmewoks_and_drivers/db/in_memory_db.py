# ===== src/frameworks_and_drivers/db/in_memory_db.py =====
import uuid
from src.entities.product import Product


class InMemoryDB:
    def __init__(self):
        self.data: list[Product] = []

    def insert(self, product: Product) -> None:
        self.data.append(product)

    def find_by_id(self, id_product: uuid.UUID) -> Product | None:
        for p in self.data:
            if p.id_product == id_product:
                return p
        return None

    def list_all(self) -> list[Product]:
        return self.data