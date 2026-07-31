# ===== src/franmewoks_and_drivers/api/routes/cliente_routes.py =====
from fastapi import APIRouter, Form

from src.franmewoks_and_drivers.api.shemas.cliente_shema import LoginClienteRequestSchema
from src.franmewoks_and_drivers.db.in_memory_cliente_db import InMemoryClienteDB
from src.franmewoks_and_drivers.security.jwt_auth_service import JwtAuthService
from src.interface_adapters.repositories.cliente_repo import ClienteRepositoryImpl
from src.interface_adapters.presenters.cliente_presenters import (
    LoginClientePresenter,
    AddClientePresenter,
)
from src.interface_adapters.controllers.cliente_controllers import (
    LoginClienteController,
    AddClienteController,
)
from src.use_cases.login_cliente import LoginClienteUsecase
from src.use_cases.add_cliente import AddClienteUsecase

router = APIRouter()

_cliente_db = InMemoryClienteDB()
_auth_service = JwtAuthService()
_cliente_repository = ClienteRepositoryImpl(_cliente_db)

_login_use_case = LoginClienteUsecase(_cliente_repository, _auth_service)
_login_presenter = LoginClientePresenter()
_login_controller = LoginClienteController(_login_use_case, _login_presenter)

_add_use_case = AddClienteUsecase(_cliente_repository, _auth_service)
_add_presenter = AddClientePresenter()
_add_controller = AddClienteController(_add_use_case, _add_presenter)


@router.post("/register")
def add_cliente(
    cliente_name: str = Form(...),
    gmail: str = Form(...),
    password: str = Form(...),
    adresse: str = Form(...),
):
    return _add_controller.handle(
        cliente_name=cliente_name,
        gmail=gmail,
        password=password,
        adresse=adresse,
    )


@router.post("/login")
def login_cliente(
    gmail: str = Form(...),
    password: str = Form(...),
):
    return _login_controller.handle(gmail=gmail, password=password)