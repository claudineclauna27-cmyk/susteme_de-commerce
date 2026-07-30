# ===== src/use_cases/update_product.py =====
from dataclasses import dataclass
from typing import Optional
import uuid
from src.entities.product import Product
from src.entities.currency import Currency
from src.use_cases.interfaces.product_repo import ProductRepository
from src.use_cases.interfaces.storage import ImageStorage


@dataclass
class UpdateProductInput:
    id_product: uuid.UUID
    product_name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    currency: Optional[Currency] = None
    photo_filename: Optional[str] = None
    photo_content: Optional[bytes] = None


@dataclass
class UpdateProductOutput:
    message: str
    success: bool
    product: Optional[Product] = None


class UpdateProductUsecase:
    def __init__(self, product_repository: ProductRepository, image_storage: ImageStorage) -> None:
        # Inject the abstract repository/storage — never import a concrete class here
        self.repo = product_repository
        self.image_storage = image_storage

    def execute(self, input_data: UpdateProductInput) -> UpdateProductOutput:
        try:
            product = self.repo.find_by_id(input_data.id_product)

            if product is None:
                return UpdateProductOutput(success=False, message="Produit introuvable")

            if input_data.product_name is not None:
                product.product_name = input_data.product_name
            if input_data.price is not None:
                product.price = input_data.price
            if input_data.quantity is not None:
                product.quantity = input_data.quantity
            if input_data.currency is not None:
                product.currency = input_data.currency

            if input_data.photo_filename and input_data.photo_content:
                product.photo_url = self.image_storage.save(
                    input_data.photo_filename,
                    input_data.photo_content,
                )

            self.repo.update(product)

            return UpdateProductOutput(
                success=True,
                message=f"Produit '{product.product_name}' mis à jour avec succès !",
                product=product,
            )

        except Exception as e:
            return UpdateProductOutput(success=False, message=str(e))