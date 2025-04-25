from typing import Optional
from sqlmodel import SQLModel, Field, Column, String, Float, Integer

class House(SQLModel, table=True, extend_existing=True):
    __tablename__ = "House"   # match exactly the Supabase table name
    
    id: Optional[int] = Field(default=None, primary_key=True)
    state: Optional[str] = Field(sa_column=Column("State", String))
    city: Optional[str] = Field(sa_column=Column("City", String))
    bedroom: Optional[float] = Field(sa_column=Column("Bedroom", Float))
    bathroom: Optional[float] = Field(sa_column=Column("Bathroom", Float))
    area: Optional[float] = Field(sa_column=Column("Area", Float))
    price: Optional[float] = Field(sa_column=Column("ListedPrice", Float))
    temperature: Optional[str] = Field(sa_column=Column("Temperature", String))
    population: Optional[float] = Field(sa_column=Column("2022 Population", Float))
    crime_rate: Optional[float] = Field(sa_column=Column("2016 Crime Rate", Float))
    unemployment: Optional[float] = Field(sa_column=Column("Unemployment", Float))
    aqi_good: Optional[float] = Field(sa_column=Column("AQI%Good", Float))
    water_quality_vpv: Optional[float] = Field(sa_column=Column("WaterQualityVPV", Float))
    cost_of_living: Optional[float] = Field(sa_column=Column("Cost of Living", Float))
    avg_c2i: Optional[float] = Field(sa_column=Column("AVG C2I", Float))
    mean_income: Optional[float] = Field(sa_column=Column("MeanIncome", Float))
    quality_of_life_total_score: Optional[float] = Field(
        sa_column=Column("QualityOfLifeTotalScore", Float)
    )
    quality_of_life_quality: Optional[int] = Field(
        sa_column=Column("QualityOfLifeQualityOfLife", Integer)
    )
    quality_of_life_affordability: Optional[int] = Field(
        sa_column=Column("QualityOfLifeAffordability", Integer)
    )
    quality_of_life_economy: Optional[int] = Field(
        sa_column=Column("QualityOfLifeEconomy", Integer)
    )
    quality_of_life_education_and_health: Optional[int] = Field(
        sa_column=Column("QualityOfLifeEducationAndHealth", Integer)
    )
    quality_of_life_safety: Optional[int] = Field(
        sa_column=Column("QualityOfLifeSafety", Integer)
    )
