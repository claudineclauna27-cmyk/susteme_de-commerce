# ===== src/use_cases/interfaces/auth_service.py =====
from abc import ABC, abstractmethod


class AuthService(ABC):
    @abstractmethod
    def hash_password(self, plain_password: str) -> str:
        ...

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        ...

    @abstractmethod
    def generate_token(self, cliente_id: str) -> str:
        ...