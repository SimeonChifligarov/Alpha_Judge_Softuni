class Town:
    """
    Represents a town with a name, latitude, and longitude.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.latitude = '0°N'
        self.longitude = '0°E'

    def set_latitude(self, latitude: str) -> None:
        self.latitude = latitude

    def set_longitude(self, longitude: str) -> None:
        self.longitude = longitude

    def __repr__(self) -> str:
        return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'

# if __name__ == '__main__':
#     town_instance = Town(name=input())
#     town_instance.set_latitude(latitude=input())
#     town_instance.set_longitude(longitude=input())
#     print(town_instance)
