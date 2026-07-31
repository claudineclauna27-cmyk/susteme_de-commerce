
# ===== src/frameworks_and_drivers/api/main.py =====
import uvicorn
from fastapi import FastAPI
from src.franmewoks_and_drivers.api.routes.product_routes import router as product_routes
from src.franmewoks_and_drivers.api.routes.cliente_routes import router as cliente_router



def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(product_routes, prefix="/api", tags=["products"])
    app.include_router(cliente_router, prefix="/api/cliente", tags=["cliente"])
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8004, reload=False)