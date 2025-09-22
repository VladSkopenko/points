import pandas as pd

def check_empty_coordinates():
    df = pd.read_csv('points.csv', skiprows=2)
    
    print(f"Total columns: {len(df.columns)}")
    print(f"Column names: {list(df.columns)}")
    
    empty_lat = df.iloc[:, 51].isna().sum()
    empty_lng = df.iloc[:, 52].isna().sum()
    
    print(f"Empty latitude: {empty_lat}")
    print(f"Empty longitude: {empty_lng}")
    
    if empty_lat > 0 or empty_lng > 0:
        print("\nRows with empty coordinates:")
        empty_rows = df[(df.iloc[:, 51].isna()) | (df.iloc[:, 52].isna())]
        for index, row in empty_rows.iterrows():
            print(f"Row {index}: {row.iloc[0]} - {row.iloc[1]}")

if __name__ == "__main__":
    check_empty_coordinates()
