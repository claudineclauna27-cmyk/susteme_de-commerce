# ===== src/use_cases/interfaces/cliente_repo.py =====
from abc import ABC, abstractmethod
from src.entities.cliente import Cliente


class ClienteRepository(ABC):
    @abstractmethod
    def add(self, cliente: Cliente) -> None:
        ...

    @abstractmethod
    def find_by_gmail(self, gmail: str) -> Cliente | None:
        ...

    @abstractmethod
    def find_by_id(self, id_cliente: int) -> Cliente | None:
        ...