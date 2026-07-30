# ===== src/franmewoks_and_drivers/api/routes/product_routes.py =====
from typing import Optional
from fastapi import APIRouter, UploadFile, File, Form

from src.franmewoks_and_drivers.db.in_memory_db import InMemoryDB
from src.franmewoks_and_drivers.storage.local_image_storage import LocalImageStorage
from src.interface_adapters.repositories.product_repo import ProductRepositoryImpl
from src.interface_adapters.presenters.presenters import AddProductPresenter
from src.interface_adapters.controllers.controllers import AddProductController
from src.use_cases.add_product import AddProductUsecase

router = APIRouter()

# Câblage des dépendances (instances partagées tant que le serveur tourne)
_db = InMemoryDB()
_image_storage = LocalImageStorage()
_repository = ProductRepositoryImpl(_db)
_use_case = AddProductUsecase(_repository, _image_storage)
_presenter = AddProductPresenter()
_controller = AddProductController(_use_case, _presenter)


@router.post("/products")
async def add_product(
    product_name: str = Form(...),
    price: float = Form(...),
    quantity: int = Form(...),
    photo: Optional[UploadFile] = File(default=None),
):
    photo_content = await photo.read() if photo else None
    photo_filename = photo.filename if photo else None

    return _controller.handle(
        product_name=product_name,
        price=price,
        quantity=quantity,
        photo_filename=photo_filename,
        photo_content=photo_content,
    )