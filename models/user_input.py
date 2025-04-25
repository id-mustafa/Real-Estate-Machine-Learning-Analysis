from typing import Literal, Optional
from sqlmodel import SQLModel
import pandas as pd

class UserInput(SQLModel, table=False):
    desired_home_price: Optional[int]
    income: Optional[int]
    bedroom: Optional[int]
    bathroom: Optional[int]
    area: Optional[int]
    population: Optional[Literal['small', 'medium', 'large']] = None
