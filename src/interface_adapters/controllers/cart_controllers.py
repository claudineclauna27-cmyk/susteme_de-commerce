# ===== src/interface_adapters/controllers/cart_controllers.py =====
import uuid
from src.use_cases.add_to_cart import AddToCartInput, AddToCartUsecase
from src.interface_adapters.presenters.cart_presenters import AddToCartPresenter


class AddToCartController:
    def __init__(self, use_case: AddToCartUsecase, presenter: AddToCartPresenter) -> None:
        self.use_case = use_case
        self.presenter = presenter

    def handle(self, id_cliente: int, id_product: uuid.UUID, quantity: int) -> dict:
        input_data = AddToCartInput(
            id_cliente=id_cliente,
            id_product=id_product,
            quantity=quantity,
        )
        output = self.use_case.execute(input_data)
        return self.presenter.present(output)