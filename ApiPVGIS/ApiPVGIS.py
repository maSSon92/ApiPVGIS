import requests

BASE_URL = "https://re.jrc.ec.europa.eu/api/seriescalc"

def get_data(latitude, longitude, start_year="2015", end_year="2016", time_step="1h", angle="35", aspect="180", peakpower="1", loss="14", outputformat="csv"):
    parameters = {
        "lat": latitude,
        "lon": longitude,
        "startyear": start_year,
        "endyear": end_year,
        "time_step": time_step,
        "angle": angle,
        "aspect": aspect,
        "peakpower": peakpower,
        "loss": loss,
        "outputformat": outputformat
    }

    pelny_url = BASE_URL + "?" + "&".join(f"{k}={v}" for k, v in parameters.items())
    print("Wysylane zapytanie do URL:", pelny_url)

    response = requests.get(BASE_URL, params=parameters)
    
    if response.status_code == 200:
        return response.text
    else:
        print("Error during data retrieval:", response.status_code, "Response content:", response.text)
        return None

def save_to_csv(data):
    with open("PVGIS_data.csv", "w", encoding="utf-8") as file:
        file.write(data)

def main():
    print("Program for retrieving PV data from PVGIS 5.2")
    
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    
    data = get_data(latitude, longitude)
    
    if data:
        save_to_csv(data)
        print("Data has been saved to PVGIS_data.csv.")

if __name__ == "__main__":
    main()
