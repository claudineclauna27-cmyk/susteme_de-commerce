# ===== src/use_cases/login_cliente.py =====
from dataclasses import dataclass
from typing import Optional
from src.use_cases.interfaces.cliente_repo import ClienteRepository
from src.use_cases.interfaces.auth_service import AuthService


@dataclass
class LoginClienteInput:
    gmail: str
    password: str


@dataclass
class LoginClienteOutput:
    message: str
    success: bool
    token: Optional[str] = None


class LoginClienteUsecase:
    def __init__(self, cliente_repository: ClienteRepository, auth_service: AuthService) -> None:
        # Inject the abstract repository/service — never import a concrete class here
        self.repo = cliente_repository
        self.auth_service = auth_service

    def execute(self, input_data: LoginClienteInput) -> LoginClienteOutput:
        try:
            cliente = self.repo.find_by_gmail(input_data.gmail)

            if cliente is None:
                return LoginClienteOutput(success=False, message="Cliente introuvable")

            if not self.auth_service.verify_password(input_data.password, cliente.password):
                return LoginClienteOutput(success=False, message="Mot de passe incorrect")

            token = self.auth_service.generate_token(str(cliente.id_cliente))

            return LoginClienteOutput(success=True, message="Connexion réussie", token=token)

        except Exception as e:
            return LoginClienteOutput(success=False, message=str(e))