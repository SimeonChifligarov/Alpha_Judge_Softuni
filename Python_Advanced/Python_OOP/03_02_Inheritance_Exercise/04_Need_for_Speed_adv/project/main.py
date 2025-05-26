from project.vehicle import Vehicle
from project.car import Car
from project.family_car import FamilyCar
from project.sport_car import SportCar
from project.motorcycle import Motorcycle
from project.cross_motorcycle import CrossMotorcycle
from project.race_motorcycle import RaceMotorcycle

if __name__ == '__main__':
    vehicle_instance = Vehicle(fuel=100.0, horse_power=120)
    car_instance = Car(fuel=60.0, horse_power=150)
    family_car_instance = FamilyCar(fuel=70.0, horse_power=140)
    sport_car_instance = SportCar(fuel=50.0, horse_power=300)
    motorcycle_instance = Motorcycle(fuel=40.0, horse_power=100)
    cross_motorcycle_instance = CrossMotorcycle(fuel=35.0, horse_power=90)
    race_motorcycle_instance = RaceMotorcycle(fuel=30.0, horse_power=110)

    # example test prints
    # print(vehicle_instance)
    # print(car_instance)
    # print(family_car_instance)
    # print(sport_car_instance)
    # print(motorcycle_instance)
    # print(cross_motorcycle_instance)
    # print(race_motorcycle_instance)
    pass
