"""
Need to create a df from the tables that we have in supabase.
- This is based on Housing Data 2

First thing is to create a service class to work with the data.
"""
# models.py
from sqlmodel import SQLModel, Field, Column, String, Float, Integer
from typing import Optional

class HousingData2(SQLModel, table=True, extend_existing=True):
    __tablename__ = "Housing Data 2"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    state: Optional[str] = Field(sa_column=Column("State", String))
    city: Optional[str]  = Field(sa_column=Column("City",  String))
    bedroom: Optional[float] = Field(sa_column=Column("Bedroom", Float))
    bathroom: Optional[float] = Field(sa_column=Column("Bathroom",Float))
    area: Optional[float] = Field(sa_column=Column("Area", Float))
    lot_area: Optional[float] = Field(sa_column=Column("LotArea", Float))
    price: Optional[float] = Field(sa_column=Column("Price", Float))
    temperature: Optional[int] = Field(sa_column=Column("Temperature", Integer))
    crime_rate: Optional[float] = Field(sa_column=Column("2016 Crime Rate", Float))
    unemployment: Optional[float] = Field(sa_column=Column("Unemployment", Float))
    aqi_good: Optional[float] = Field(sa_column=Column("AQI%Good", Float))
    water_quality_vpv: Optional[float] = Field(sa_column=Column("WaterQualityVPV", Float))
    cost_of_living: Optional[float] = Field(sa_column=Column("Cost of Living", Float))
    median_income_2022: Optional[float] = Field(sa_column=Column("2022 Median Income",Float))
    population: Optional[float] = Field(sa_column=Column("Population", Float))
