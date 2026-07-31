# ===== src/franmewoks_and_drivers/security/jwt_auth_service.py =====
import bcrypt
import jwt
from datetime import datetime, timedelta
from src.use_cases.interfaces.auth_service import AuthService

SECRET_KEY = "change-moi-en-vraie-cle-secrete"


class JwtAuthService(AuthService):
    def hash_password(self, plain_password: str) -> str:
        hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    def generate_token(self, cliente_id: str) -> str:
        payload = {
            "cliente_id": cliente_id,
            "exp": datetime.utcnow() + timedelta(hours=2),
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")