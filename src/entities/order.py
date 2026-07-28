from dataclasses import dataclass, field
from datetime import date
import uuid

dataclass
class Order:
    id_order : uuid.UUID = field(default_factory=uuid.uuid4) 
    oder_date : date 
    total_amout : float 

    def __post_init__(self):
        if self.id_order <= 0 :
            raise ValueError("better to avoid negative ")
        if self.oder_date > date.today():
            raise ValueError("you can't make a oder in the furure ")
        if self.total_amout <= 0 :
            raise ValueError("Total amout must be positive")
        

