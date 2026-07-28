from dataclasses import dataclass


@dataclass
class Category:
    id_category : int
    category_name : str

    def __post_init__(self):
        if not self.category_name or not self.category_name.strip():
            raise ValueError ("cant not be empty ")