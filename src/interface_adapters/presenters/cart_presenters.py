# ===== src/interface_adapters/presenters/cart_presenters.py =====
from src.use_cases.add_to_cart import AddToCartOutput


class AddToCartPresenter:
    def present(self, output: AddToCartOutput) -> dict:
        if output.success:
            return {
                "success": True,
                "message": output.message,
                "cart": {
                    "id_cliente": output.cart.id_cliente,
                    "items": [
                        {
                            "id_product": str(item.id_product),
                            "product_name": item.product_name,
                            "price": item.price,
                            "currency": item.currency.value,
                            "quantity": item.quantity,
                            "subtotal": item.price * item.quantity,
                        }
                        for item in output.cart.items
                    ],
                    "total_by_currency": output.cart.total_by_currency(),
                },
            }
        return {"success": False, "message": output.message}