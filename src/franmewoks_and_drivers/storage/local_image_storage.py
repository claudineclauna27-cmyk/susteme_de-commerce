# ===== src/frameworks_and_drivers/storage/local_image_storage.py =====
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
        return filepath