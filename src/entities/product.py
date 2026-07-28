from dataclasses import dataclass, field
from enum import Enum
import uuid

class Currency(Enum):
    HTG = "HTG"


@dataclass
class Product:
    id_product : uuid.UUID = field(default_factory=uuid.uuid4)
    product_name : str 
    quantity : int 
    price : float 
    currency = Currency
    

    def __post_init__(self):
        if not self.product_name or not self.product_name.strip():
            raise ValueError ("please enter the name ")
        if self.price < 0 :
            raise ValueError("price can't be negative ")
        if self.quantity <=0 :
            raise ValueError ("quantity must be positive ")

        