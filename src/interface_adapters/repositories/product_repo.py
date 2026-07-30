# ===== src/interface_adapter/repository/product_repository_impl.py =====
import uuid
from src.use_cases.interfaces.product_repo import ProductRepository
from src.entities.product import Product


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, db):
        self.db = db

    def add(self, product: Product) -> None:
        self.db.insert(product)

    def find_by_id(self, id_product: uuid.UUID) -> Product | None:
        return self.db.find_by_id(id_product)

    def list_all(self) -> list[Product]:
        return self.db.list_all()