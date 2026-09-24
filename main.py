from extract import extract_data
from transform import formatting, dedupe, dropping, filling
from load import load

if __name__ == "__main__":
    df = extract_data()
    df = formatting(df)
    df = dedupe(df)
    df = dropping(df)
    df = filling(df)
    df = load(df)
    print(df)