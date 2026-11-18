import httpx
from pydantic import BaseModel

URL = "https://api.open-meteo.com/v1/forecast"


class CurrentWeather(BaseModel):
    time: str
    temperature_2m: float
    wind_speed_10m: float


class Forecast(BaseModel):
    latitude: float
    longitude: float
    current: CurrentWeather

def get_forecast(latitude: float, longitude: float) -> Forecast:
    response = httpx.get(
        URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m",
        },
        timeout=10,
    )
    response.raise_for_status()
    return Forecast.model_validate(response.json())


# PART 01:)

# # KARACHI
# karachi = get_forecast(24.86, 67.01)
# print(f"{karachi.current.temperature_2m}°C, wind {karachi.current.wind_speed_10m} km/h")


# # LAHORE
# lahore = get_forecast(31.55, 74.34)
# print(f"{lahore.current.temperature_2m}°C, wind {lahore.current.wind_speed_10m} km/h")


# # ISLAMABAD
# islamabad = get_forecast(33.69, 73.06)
# print(f"{islamabad.current.temperature_2m}°C, wind {islamabad.current.wind_speed_10m} km/h")


# # QUETTA
# quetta = get_forecast(30.18, 66.98)
# print(f"{quetta.current.temperature_2m}°C, wind {quetta.current.wind_speed_10m} km/h")



CITIES = {
    "Karachi": (24.86, 67.01),
    "Lahore": (31.55, 74.34),
    "Islamabad": (33.69, 73.06),
    "Quetta": (30.18, 66.98),
    "ABCDE": (95,45),

}

# for city, coordinates in CITIES.items():
#     forecast = get_forecast(coordinates[0], coordinates[1])

#     print(f"{city}: {forecast.current.temperature_2m}°C")


# PART 02:)


# Get weather for each city
for city, coordinates in CITIES.items():

    try:
        forecast = get_forecast(coordinates[0], coordinates[1])

        print(
            f"{city}: {forecast.current.temperature_2m}°C"
        )

    except httpx.HTTPStatusError as error:
        print(
            f"{city}: API error "
            f"{error.response.status_code} - {error.response.text}"
        )

    except httpx.RequestError as error:
        print(
            f"{city}: Connection error - {error}"
        )
