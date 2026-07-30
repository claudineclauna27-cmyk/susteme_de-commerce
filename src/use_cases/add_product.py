# ===== src/usecase/add_product.py =====
from dataclasses import dataclass
from typing import Optional
from src.entities.product import Product
from src.use_cases.interfaces.product_repo import ProductRepository
from src.use_cases.interfaces.storage import ImageStorage


@dataclass
class AddProductInput:
    Product_name: str
    price: float
    quantity: int
    photo_filename: Optional[str] = None
    photo_content: Optional[bytes] = None


@dataclass
class AddProductOutput:
    message: str
    success: bool
    product: Optional[Product] = None


class AddProductUsecase:
    def __init__(self, product_repository: ProductRepository, image_storage: ImageStorage) -> None:
        # Inject the abstract repository/storage — never import a concrete class here
        self.repo = product_repository
        self.image_storage = image_storage

    def execute(self, input_data: AddProductInput) -> AddProductOutput:
        try:
            photo_url = None

            if input_data.photo_filename and input_data.photo_content:
                photo_url = self.image_storage.save(
                    input_data.photo_filename,
                    input_data.photo_content,
                )

            product = Product(
                product_name=input_data.Product_name,
                price=input_data.price,
                quantity=input_data.quantity,
                photo_url=photo_url,
            )

            self.repo.add(product)

            return AddProductOutput(
                success=True,
                message=f"Produit '{product.product_name}' ajouté avec succès !",
                product=product,
            )

        except Exception as e:
            return AddProductOutput(success=False, message=str(e))