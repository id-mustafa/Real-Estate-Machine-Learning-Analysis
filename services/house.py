
from sqlmodel import SQLModel, create_engine, Session, select
import pandas as pd
from models.housingdata import HousingData2
from models.house import House

class HouseService:
    """_summary_
    HousingService is meant to store all the helper functions related to working with our datasets, so it should
    streamline the project without getting in the way of the machine learning aspect. 
    
    It is initialized in a parent notebook that takes in a session and can interact with the database directly
    for whatever we need to do. Having this class cleans up our code and avoids duplicate work.
    """
    def __init__(self, session: Session):
        self.session = session

    def get_house_data_df(self) -> pd.DataFrame:
        """Pull all rows from HousingData into a DataFrame"""
        rows = self.session.exec(select(House)).all()
        return pd.DataFrame([r.model_dump() for r in rows])

    def get_housing_data2_df(self) -> pd.DataFrame:
        """Pull all rows from HousingData2 into a DataFrame"""
        rows = self.session.exec(select(HousingData2)).all()
        return pd.DataFrame([r.model_dump() for r in rows])
    
    @staticmethod
    def save_house_data_to_csvs(house_data: pd.DataFrame, housing_data: pd.DataFrame):
        """
        Saves the 'House' table to the given CSV path (default ../data/house.csv)
        in case we hit rate limits with Supabase.
        """
        for df, path in [(house_data, "../data/house_data.csv"), (housing_data, "../data/housing_data2.csv")]:
            df.to_csv(path, index=False)
            print(f"House data saved to {path}")

    @staticmethod
    def categorize_pop_by_quantile(s: pd.Series) -> pd.Series:
        """
        Splits the series into three equal‐sized bins (tertiles) 
        labeled 'small', 'medium', 'large' based on its distribution.
        """
        return pd.qcut(s, q=3, labels=['small','medium','large'])