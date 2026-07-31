# ===== src/use_cases/list_products.py =====
from dataclasses import dataclass
from src.entities.product import Product
from src.use_cases.interfaces.product_repo import ProductRepository


@dataclass
class ListProductsOutput:
    success: bool
    products: list[Product]
    message: str = ""


class ListProductsUsecase:
    def __init__(self, product_repository: ProductRepository) -> None:
        # Inject the abstract repository — never import a concrete class here
        self.repo = product_repository

    def execute(self) -> ListProductsOutput:
        try:
            products = self.repo.list_all()
            return ListProductsOutput(success=True, products=products)
        except Exception as e:
            return ListProductsOutput(success=False, products=[], message=str(e))