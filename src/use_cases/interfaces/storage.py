# ===== src/usecase/interfaces/image_storage.py =====
from abc import ABC, abstractmethod


class ImageStorage(ABC):
    @abstractmethod
    def save(self, filename: str, content: bytes) -> str:
        """Sauvegarde l'image et retourne son URL/chemin d'accès."""
        ...

    @abstractmethod
    def delete(self, photo_url: str) -> None:
        ...