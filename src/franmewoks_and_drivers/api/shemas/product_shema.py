# ===== src/frameworks_and_drivers/api/schemas/product_schema.py =====
from pydantic import BaseModel
from typing import Optional


class AddProductResponseSchema(BaseModel):
    success: bool
    message: str
    product: Optional[dict] = None