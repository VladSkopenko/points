import googlemaps
import os
import pandas as pd
from typing import Tuple, Optional

def get_coordinates_from_address(address: str, api_key: str) -> Optional[Tuple[float, float]]:
    try:
        gmaps = googlemaps.Client(key=api_key)
        geocode_result = gmaps.geocode(address)
        
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            return None
            
    except Exception as e:
        print(e)
        return None

def main():
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    
    if not api_key:
        return
    
    df = pd.read_csv('points.csv', skiprows=2)
    
    for index, row in df.iterrows():
        if pd.notna(row['Адреса']) and row['Адреса'].strip():
            print(f"Processing: {row['Адреса']}")
            coordinates = get_coordinates_from_address(row['Адреса'], api_key)
            if coordinates:
                lat, lng = coordinates
                df.iloc[index, 50] = lat
                df.iloc[index, 51] = lng
                print(f"Found: {lat}, {lng}")
            else:
                print("Not found")
    
    df.to_csv('points.csv', index=False)

if __name__ == "__main__":
    main()
