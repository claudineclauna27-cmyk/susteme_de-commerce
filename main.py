# ===== src/franmewoks_and_drivers/api/main.py =====
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.franmewoks_and_drivers.api.routes.product_routes import router as product_router
from src.franmewoks_and_drivers.api.routes.cliente_routes import router as cliente_router
from src.franmewoks_and_drivers.api.routes.cart_routes import router as cart_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
    app.include_router(product_router, prefix="/api", tags=["products"])
    app.include_router(cliente_router, prefix="/api/cliente", tags=["cliente"])
    app.include_router(cart_router, prefix="/api", tags=["cart"])
    return app

# ===== main.py (racine C:\Users\claud\Systeme_commerce\main.py) =====
import uvicorn


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8004, reload=False)