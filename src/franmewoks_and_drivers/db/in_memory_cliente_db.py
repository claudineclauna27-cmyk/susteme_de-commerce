from src.entities.cliente import Cliente


class InMemoryClienteDB:
    def __init__(self):
        self.data: list[Cliente] = []
        self._next_id = 1   # compteur auto-incrémenté

    def insert(self, cliente: Cliente) -> None:
        cliente.id_cliente = self._next_id
        self._next_id += 1
        self.data.append(cliente)

    def find_by_gmail(self, gmail: str) -> Cliente | None:
        for c in self.data:
            if c.gmail == gmail:
                return c
        return None

    def find_by_id(self, id_cliente: int) -> Cliente | None:
        for c in self.data:
            if c.id_cliente == id_cliente:
                return c
        return None