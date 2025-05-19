class Vehicle:
    """
    This class is for a vehicle. It stores the maximum speed, mileage, and gadgets.

    Args:
        max_speed (int, optional): The top speed of the vehicle. Defaults to 150.
        mileage (float): The distance the vehicle has traveled
    """

    def __init__(self, mileage: float, max_speed: int = 150) -> None:
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []

# if __name__ == '__main__':
#     vehicle_mileage = 12345.6
#     vehicle_instance = Vehicle(mileage=vehicle_mileage)
#     print(vehicle_instance.max_speed)
#     print(vehicle_instance.mileage)
#     print(vehicle_instance.gadgets)
#     vehicle_instance.gadgets.append('GPS')
#     print(vehicle_instance.gadgets)
