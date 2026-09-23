import pandas as pd

def extract_data():
    """ Function to extract data from a source."""

    data = pd.read_csv("data/messy_sales_sample.csv")
    return data

if __name__ == "__main__":
    df = extract_data()
    print(df)
