# ===== src/use_cases/add_cliente.py =====
from dataclasses import dataclass
from typing import Optional
from src.entities.cliente import Cliente
from src.use_cases.interfaces.cliente_repo import ClienteRepository
from src.use_cases.interfaces.auth_service import AuthService


@dataclass
class AddClienteInput:
    cliente_name: str
    gmail: str
    password: str
    adresse: str


@dataclass
class AddClienteOutput:
    message: str
    success: bool
    cliente: Optional[Cliente] = None


class AddClienteUsecase:
    def __init__(self, cliente_repository: ClienteRepository, auth_service: AuthService) -> None:
        # Inject the abstract repository/service — never import a concrete class here
        self.repo = cliente_repository
        self.auth_service = auth_service

    def execute(self, input_data: AddClienteInput) -> AddClienteOutput:
        try:
            existing = self.repo.find_by_gmail(input_data.gmail)
            if existing is not None:
                return AddClienteOutput(success=False, message="Cet email est déjà utilisé")

            hashed_password = self.auth_service.hash_password(input_data.password)

            cliente = Cliente(
                cliente_name=input_data.cliente_name,
                gmail=input_data.gmail,
                password=hashed_password,
                adresse=input_data.adresse,
            )

            self.repo.add(cliente)

            return AddClienteOutput(
                success=True,
                message=f"Compte créé pour '{cliente.cliente_name}' avec succès !",
                cliente=cliente,
            )

        except Exception as e:
            return AddClienteOutput(success=False, message=str(e))