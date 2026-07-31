# ===== src/franmewoks_and_drivers/storage/local_image_storage.py =====
import os
from src.use_cases.interfaces.storage import ImageStorage


class LocalImageStorage(ImageStorage):
    def __init__(self, upload_dir: str = "uploads/products"):
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)

    def save(self, filename: str, content: bytes) -> str:
        filepath = os.path.join(self.upload_dir, filename)
        with open(filepath, "wb") as f:
            f.write(content)

        # Retourne une URL accessible via navigateur, pas un chemin disque brut
        url_path = f"/{self.upload_dir}/{filename}".replace("\\", "/")
        return url_path

    def delete(self, photo_url: str) -> None:
        # photo_url ressemble à "/uploads/products/riz.jpg"
        filepath = photo_url.lstrip("/")
        if filepath and os.path.exists(filepath):
            os.remove(filepath)