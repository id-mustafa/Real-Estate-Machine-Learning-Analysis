from typing import Literal
from sqlmodel import SQLModel
import pandas as pd

class UserInput(SQLModel, table=False):
    desired_home_price: int
    income: int
    bedroom: int
    bathroom: int
    area: int
    population: Literal['small', 'medium', 'large'] = None
