from dataclasses import dataclass


@dataclass
class Admin:
    id_admin : int 
    admin_name : str


    def __post_init__(self):
        if not self.admin_name or not self.admin_name.strip():
            raise ValueError ("can not be empty ")