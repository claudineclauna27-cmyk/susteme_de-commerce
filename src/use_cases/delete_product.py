# ===== src/use_cases/delete_product.py =====
from dataclasses import dataclass
import uuid
from src.use_cases.interfaces.product_repo import ProductRepository
from src.use_cases.interfaces.storage import ImageStorage


@dataclass
class DeleteProductInput:
    id_product: uuid.UUID


@dataclass
class DeleteProductOutput:
    message: str
    success: bool


class DeleteProductUsecase:
    def __init__(self, product_repository: ProductRepository, image_storage: ImageStorage) -> None:
        # Inject the abstract repository/storage — never import a concrete class here
        self.repo = product_repository
        self.image_storage = image_storage

    def execute(self, input_data: DeleteProductInput) -> DeleteProductOutput:
        try:
            product = self.repo.find_by_id(input_data.id_product)

            if product is None:
                return DeleteProductOutput(success=False, message="Produit introuvable")

            if product.photo_url:
                self.image_storage.delete(product.photo_url)

            self.repo.delete(input_data.id_product)

            return DeleteProductOutput(
                success=True,
                message=f"Produit '{product.product_name}' supprimé avec succès !",
            )

        except Exception as e:
            return DeleteProductOutput(success=False, message=str(e))