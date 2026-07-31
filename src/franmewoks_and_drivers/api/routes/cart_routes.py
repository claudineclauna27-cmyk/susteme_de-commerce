# ===== src/franmewoks_and_drivers/api/routes/cart_routes.py =====
import uuid
from fastapi import APIRouter, Form

from src.franmewoks_and_drivers.db.in_memory_cart_db import InMemoryCartDB
from src.interface_adapters.repositories.cart_repo import CartRepositoryImpl
from src.interface_adapters.presenters.cart_presenters import AddToCartPresenter
from src.interface_adapters.controllers.cart_controllers import AddToCartController
from src.use_cases.add_to_cart import AddToCartUsecase

# Réutilise la même instance de repository produit que product_routes.py
from src.franmewoks_and_drivers.api.routes.product_routes import _repository as _product_repository

router = APIRouter()

_cart_db = InMemoryCartDB()
_cart_repository = CartRepositoryImpl(_cart_db)

_add_to_cart_use_case = AddToCartUsecase(_cart_repository, _product_repository)
_add_to_cart_presenter = AddToCartPresenter()
_add_to_cart_controller = AddToCartController(_add_to_cart_use_case, _add_to_cart_presenter)


@router.post("/cart/add")
def add_to_cart(
    id_cliente: int = Form(...),
    id_product: uuid.UUID = Form(...),
    quantity: int = Form(...),
):
    return _add_to_cart_controller.handle(
        id_cliente=id_cliente,
        id_product=id_product,
        quantity=quantity,
    )