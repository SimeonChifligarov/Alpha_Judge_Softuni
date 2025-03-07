class Town:
    def __init__(self, name: str):
        """Initializes the town with a name, default latitude '0°N', and default longitude '0°E'."""
        self.name = name
        self.latitude = '0°N'
        self.longitude = '0°E'

    def set_latitude(self, latitude: str):
        """Sets the latitude of the town."""
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        """Sets the longitude of the town."""
        self.longitude = longitude

    def __repr__(self) -> str:
        """Returns a formatted string representation of the town with its coordinates."""
        return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'
