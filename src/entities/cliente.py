from dataclasses import dataclass


@dataclass
class Cliente:
    id_client : int 
    cliente_name : str 
    gmail : str 
    password : str 
    adress : str 

    def __post_init__(self):
        if not self.cliente_name or not self.cliente_name.strip():
            raise ValueError("You must add your Name ")
        if not self.gmail or "@" not in self.gmail:
            raise ValueError ("Invalid gmail")
        if not self.password:
            raise ValueError ("Password is required ")