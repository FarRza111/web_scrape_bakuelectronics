import typing as ty
from typing import Literal
from dataclasses import dataclass
import os
import pandas as pd
from pydantic import *
data = pd.read_excel(os.path.join(os.getcwd(), '_data_.xlsx'))


@dataclass
class Bina:
    model: ty.Optional[str]
    price: int

    def __post_init__(self):
        if isinstance(self.price, str):
            raise TypeError("string is not valid attr for price")


Item = Bina('Fariz', 37)
print(Item)








#








