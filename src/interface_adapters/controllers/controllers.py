# ===== src/interface_adapter/controllers/add_product_controller.py =====
from typing import Optional
from src.use_cases.add_product import AddProductInput, AddProductUsecase
from src.interface_adapters.presenters.presenters import AddProductPresenter


class AddProductController:
    def __init__(self, use_case: AddProductUsecase, presenter: AddProductPresenter) -> None:
        self.use_case = use_case
        self.presenter = presenter

    def handle(
        self,
        product_name: str,
        price: float,
        quantity: int,
        photo_filename: Optional[str] = None,
        photo_content: Optional[bytes] = None,
    ) -> dict:
        input_data = AddProductInput(
            Product_name=product_name,
            price=price,
            quantity=quantity,
            photo_filename=photo_filename,
            photo_content=photo_content,
        )
        output = self.use_case.execute(input_data)
        return self.presenter.present(output)