# ===== src/interface_adapters/controllers/cliente_controllers.py =====
from src.use_cases.login_cliente import LoginClienteInput, LoginClienteUsecase
from src.use_cases.add_cliente import AddClienteInput, AddClienteUsecase
from src.interface_adapters.presenters.cliente_presenters import LoginClientePresenter, AddClientePresenter


class LoginClienteController:
    def __init__(self, use_case: LoginClienteUsecase, presenter: LoginClientePresenter) -> None:
        self.use_case = use_case
        self.presenter = presenter

    def handle(self, gmail: str, password: str) -> dict:
        input_data = LoginClienteInput(gmail=gmail, password=password)
        output = self.use_case.execute(input_data)
        return self.presenter.present(output)


class AddClienteController:
    def __init__(self, use_case: AddClienteUsecase, presenter: AddClientePresenter) -> None:
        self.use_case = use_case
        self.presenter = presenter

    def handle(self, cliente_name: str, gmail: str, password: str, adresse: str) -> dict:
        input_data = AddClienteInput(
            cliente_name=cliente_name,
            gmail=gmail,
            password=password,
            adresse=adresse,
        )
        output = self.use_case.execute(input_data)
        return self.presenter.present(output)