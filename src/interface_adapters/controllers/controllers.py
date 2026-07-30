# ===== src/interface_adapters/controllers/controllers.py =====
from typing import Optional
import uuid
from src.use_cases.add_product import AddProductInput, AddProductUsecase
from src.use_cases.update_product import UpdateProductInput, UpdateProductUsecase
from src.entities.currency import Currency
from src.interface_adapters.presenters.presenters import AddProductPresenter, UpdateProductPresenter


class AddProductController:
    def __init__(self, use_case: AddProductUsecase, presenter: AddProductPresenter) -> None:
        self.use_case = use_case
        self.presenter = presenter

    def handle(
        self,
        product_name: str,
        price: float,
        quantity: int,
        currency: Currency,
        photo_filename: Optional[str] = None,
        photo_content: Optional[bytes] = None,
    ) -> dict:
        input_data = AddProductInput(
            Product_name=product_name,
            price=price,
            quantity=quantity,
            currency=currency,
            photo_filename=photo_filename,
            photo_content=photo_content,
        )
        output = self.use_case.execute(input_data)
        return self.presenter.present(output)


class UpdateProductController:
    def __init__(self, use_case: UpdateProductUsecase, presenter: UpdateProductPresenter) -> None:
        self.use_case = use_case
        self.presenter = presenter

    def handle(
        self,
        id_product: uuid.UUID,
        product_name: Optional[str] = None,
        price: Optional[float] = None,
        quantity: Optional[int] = None,
        currency: Optional[Currency] = None,
        photo_filename: Optional[str] = None,
        photo_content: Optional[bytes] = None,
    ) -> dict:
        input_data = UpdateProductInput(
            id_product=id_product,
            product_name=product_name,
            price=price,
            quantity=quantity,
            currency=currency,
            photo_filename=photo_filename,
            photo_content=photo_content,
        )
        output = self.use_case.execute(input_data)
        return self.presenter.present(output)