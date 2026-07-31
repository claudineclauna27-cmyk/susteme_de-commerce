# ===== src/interface_adapters/repositories/cliente_repo.py =====
import uuid
from src.use_cases.interfaces.cliente_repo import ClienteRepository
from src.entities.cliente import Cliente


class ClienteRepositoryImpl(ClienteRepository):
    def __init__(self, db):
        self.db = db

    def add(self, cliente: Cliente) -> None:
        self.db.insert(cliente)

    def find_by_gmail(self, gmail: str) -> Cliente | None:
        return self.db.find_by_gmail(gmail)

    def find_by_id(self, id_cliente: uuid.UUID) -> Cliente | None:
        return self.db.find_by_id(id_cliente)