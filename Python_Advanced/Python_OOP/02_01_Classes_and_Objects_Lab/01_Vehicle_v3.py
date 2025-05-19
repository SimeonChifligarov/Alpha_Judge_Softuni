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

    def __str__(self) -> str:
        return f'Vehicle with max speed {self.max_speed} and mileage {self.mileage}.'

    def __repr__(self) -> str:
        return f'Vehicle(max_speed={self.max_speed!r}, mileage={self.mileage!r}, gadgets={self.gadgets!r})'

    # def __repr__(self) -> str:
    #     cls_name = self.__class__.__name__
    #     attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
    #     return f'{cls_name}({attrs})'

    def __len__(self) -> int:
        return len(self.gadgets)

    def __bool__(self) -> bool:
        return bool(self.gadgets)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vehicle):
            return (self.max_speed, self.mileage) == (other.max_speed, other.mileage)
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Vehicle):
            return self.max_speed > other.max_speed
        return NotImplemented

# if __name__ == '__main__':
#     vehicle_mileage_1 = 10000.0
#     vehicle_mileage_2 = 20000.0
#     vehicle_1 = Vehicle(mileage=vehicle_mileage_1, max_speed=180)
#     vehicle_2 = Vehicle(mileage=vehicle_mileage_2, max_speed=150)
#     print(vehicle_1 == vehicle_2)
#     print(vehicle_1 > vehicle_2)
#     print(str(vehicle_1))
#     print(repr(vehicle_2))
#     vehicle_1.gadgets.append('Camera')
#     print(len(vehicle_1))
#     print(bool(vehicle_1))
