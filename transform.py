import pandas as pd
from extract import extract_data

def formatting(data):
    """Function to formatting the messy data"""
    data['Region'] = data['Region'].str.strip().str.capitalize()
    data['Sales Rep'] = data['Sales Rep'].str.strip().str.capitalize()
    return data
def dedupe(data):
    """Function to delete the duplicate rows available in the dataframe"""
    data = data.drop_duplicates().reset_index(drop=True)
    return data
def dropping(data):
    """Function to dropping the unwanted rows"""
    data = data.dropna(subset=['Sales Rep']).reset_index(drop=True)
    return data
def filling(data):
    """Function to fill the missing values"""
    units_mean = data['Units Sold'].mean()
    revenue_mean = data['Revenue'].mean()
    data = data.fillna({'Units Sold': units_mean, 'Revenue': revenue_mean})
    return data

if __name__ == "__main__":
    df = formatting(extract_data())
    df = dedupe(df)
    df = dropping(df)
    df = filling(df)
    print(df)