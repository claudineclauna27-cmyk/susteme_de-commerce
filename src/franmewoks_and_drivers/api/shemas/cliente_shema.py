# ===== src/franmewoks_and_drivers/api/shemas/cliente_shema.py =====
from pydantic import BaseModel


class LoginClienteRequestSchema(BaseModel):
    gmail: str
    password: str


class AddClienteRequestSchema(BaseModel):
    cliente_name: str
    gmail: str
    password: str
    adresse: str