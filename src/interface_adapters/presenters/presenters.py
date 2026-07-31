# ===== src/interface_adapter/presenters/add_product_presenter.py =====
from src.use_cases.add_product import AddProductOutput
from src.use_cases.update_product import UpdateProductOutput
from src.use_cases.delete_product import DeleteProductOutput


class AddProductPresenter:
    def present(self, output: AddProductOutput) -> dict:
        if output.success:
            return {
                "success": True,
                "message": output.message,
                "product": {
                    "id_product": str(output.product.id_product),
                    "product_name": output.product.product_name,
                    "price": output.product.price,
                    "quantity": output.product.quantity,
                    "photo_url": output.product.photo_url,
                },
            }
        return {
            "success": False,
            "message": output.message,
        }



class UpdateProductPresenter:
    def present(self, output: UpdateProductOutput) -> dict:
        if output.success:
            return {
                "success": True,
                "message": output.message,
                "product": {
                    "id_product": str(output.product.id_product),
                    "product_name": output.product.product_name,
                    "price": output.product.price,
                    "currency": output.product.currency.value,
                    "quantity": output.product.quantity,
                    "photo_url": output.product.photo_url,
                },
            }
        return {"success": False, "message": output.message}


class DeleteProductPresenter:
    def present(self, output: DeleteProductOutput) -> dict:
        return {
            "success": output.success,
            "message": output.message,
        }


# ===== src/interface_adapters/presenters/presenters.py =====
# ... AddProductPresenter, UpdateProductPresenter, DeleteProductPresenter restent inchangés

from src.use_cases.list_products import ListProductsOutput


class ListProductsPresenter:
    def present(self, output: ListProductsOutput) -> dict:
        if output.success:
            return {
                "success": True,
                "products": [
                    {
                        "id_product": str(p.id_product),
                        "product_name": p.product_name,
                        "price": p.price,
                        "currency": p.currency.value,
                        "quantity": p.quantity,
                        "photo_url": p.photo_url,
                    }
                    for p in output.products
                ],
            }
        return {"success": False, "message": output.message}