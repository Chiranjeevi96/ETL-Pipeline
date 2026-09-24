import sqlite3 
import pandas as pd
from extract import extract_data
from transform import formatting, dedupe, dropping, filling

def load(data):
    database = sqlite3.connect('sales_data.db')
    data.to_sql('sales_data', database, if_exists='append', index=False)
    return data


if __name__ == "__main__":
    df = extract_data()
    df = formatting(df)
    df = dedupe(df)
    df = dropping(df)
    df = filling(df)
    df = load(df)
    print(df)

    conn = sqlite3.connect('sales_data.db')
    check = pd.read_sql('SELECT * FROM sales_data', conn)
    print(check)