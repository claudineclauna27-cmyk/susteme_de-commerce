# ===== src/use_cases/add_to_cart.py =====
from dataclasses import dataclass
from typing import Optional
import uuid
from src.entities.cart import Cart
from src.use_cases.interfaces.cart_repo import CartRepository
from src.use_cases.interfaces.product_repo import ProductRepository


@dataclass
class AddToCartInput:
    id_cliente: int
    id_product: uuid.UUID
    quantity: int


@dataclass
class AddToCartOutput:
    message: str
    success: bool
    cart: Optional[Cart] = None


class AddToCartUsecase:
    def __init__(self, cart_repository: CartRepository, product_repository: ProductRepository) -> None:
        # Inject the abstract repositories — never import a concrete class here
        self.cart_repo = cart_repository
        self.product_repo = product_repository

    def execute(self, input_data: AddToCartInput) -> AddToCartOutput:
        try:
            product = self.product_repo.find_by_id(input_data.id_product)
            if product is None:
                return AddToCartOutput(success=False, message="Produit introuvable")

            if input_data.quantity > product.quantity:
                return AddToCartOutput(success=False, message="Quantité demandée supérieure au stock disponible")

            cart = self.cart_repo.find_by_cliente(input_data.id_cliente)
            if cart is None:
                cart = Cart(id_cliente=input_data.id_cliente)

            cart.add_item(
                id_product=product.id_product,
                product_name=product.product_name,
                price=product.price,
                currency=product.currency,
                quantity=input_data.quantity,
            )
            self.cart_repo.save(cart)

            return AddToCartOutput(
                success=True,
                message=f"Produit '{product.product_name}' ajouté au panier !",
                cart=cart,
            )

        except Exception as e:
            return AddToCartOutput(success=False, message=str(e))