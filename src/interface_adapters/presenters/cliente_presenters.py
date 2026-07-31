# ===== src/interface_adapters/presenters/cliente_presenters.py =====
from src.use_cases.login_cliente import LoginClienteOutput
from src.use_cases.add_cliente import AddClienteOutput


class LoginClientePresenter:
    def present(self, output: LoginClienteOutput) -> dict:
        return {
            "success": output.success,
            "message": output.message,
            "token": output.token,
        }


class AddClientePresenter:
    def present(self, output: AddClienteOutput) -> dict:
        if output.success:
            return {
                "success": True,
                "message": output.message,
                "cliente": {
                    "id_cliente": output.cliente.id_cliente,
                    "cliente_name": output.cliente.cliente_name,
                    "gmail": output.cliente.gmail,
                    "adresse": output.cliente.adresse,
                },
            }
        return {"success": False, "message": output.message}