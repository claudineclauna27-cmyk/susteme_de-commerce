# ===== src/franmewoks_and_drivers/api/routes/product_routes.py =====
from typing import Optional
import uuid
from fastapi import APIRouter, UploadFile, File, Form

from src.entities.currency import Currency
from src.franmewoks_and_drivers.db.in_memory_db import InMemoryDB
from src.franmewoks_and_drivers.storage.local_image_storage import LocalImageStorage
from src.interface_adapters.repositories.product_repo import ProductRepositoryImpl
from src.interface_adapters.presenters.presenters import (
    AddProductPresenter,
    UpdateProductPresenter,
)
from src.interface_adapters.controllers.controllers import (
    AddProductController,
    UpdateProductController,
)
from src.use_cases.add_product import AddProductUsecase
from src.use_cases.update_product import UpdateProductUsecase

router = APIRouter()

_db = InMemoryDB()
_image_storage = LocalImageStorage()
_repository = ProductRepositoryImpl(_db)

_add_use_case = AddProductUsecase(_repository, _image_storage)
_add_presenter = AddProductPresenter()
_add_controller = AddProductController(_add_use_case, _add_presenter)

_update_use_case = UpdateProductUsecase(_repository, _image_storage)
_update_presenter = UpdateProductPresenter()
_update_controller = UpdateProductController(_update_use_case, _update_presenter)


@router.post("/products")
async def add_product(
    product_name: str = Form(...),
    price: float = Form(...),
    quantity: int = Form(...),
    currency: Currency = Form(...),
    photo: Optional[UploadFile] = File(default=None),
):
    photo_content = await photo.read() if photo else None
    photo_filename = photo.filename if photo else None

    return _add_controller.handle(
        product_name=product_name,
        price=price,
        quantity=quantity,
        currency=currency,
        photo_filename=photo_filename,
        photo_content=photo_content,
    )


@router.put("/products/{id_product}")
async def update_product(
    id_product: uuid.UUID,
    product_name: Optional[str] = Form(default=None),
    price: Optional[float] = Form(default=None),
    quantity: Optional[int] = Form(default=None),
    currency: Optional[Currency] = Form(default=None),
    photo: Optional[UploadFile] = File(default=None),
):
    photo_content = await photo.read() if photo else None
    photo_filename = photo.filename if photo else None

    return _update_controller.handle(
        id_product=id_product,
        product_name=product_name,
        price=price,
        quantity=quantity,
        currency=currency,
        photo_filename=photo_filename,
        photo_content=photo_content,
    )