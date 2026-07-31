# ===== src/entities/cliente.py =====
from dataclasses import dataclass
from typing import Optional


@dataclass
class Cliente:
    cliente_name: str
    gmail: str
    password: str
    adresse: str
    id_cliente: Optional[int] = None

    def __post_init__(self):
        if not self.cliente_name or not self.cliente_name.strip():
            raise ValueError("please enter the name")
        if not self.gmail or "@" not in self.gmail:
            raise ValueError("invalid email")
        if not self.password:
            raise ValueError("password is required")