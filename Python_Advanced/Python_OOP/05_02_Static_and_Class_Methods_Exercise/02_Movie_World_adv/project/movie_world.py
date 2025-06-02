from typing import Union
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    """This class manages a movie world where customers can rent DVDs."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer: Union[Customer, None] = self.__find_customer_by_id(customer_id=customer_id)
        dvd: Union[DVD, None] = self.__find_dvd_by_id(dvd_id=dvd_id)
        if customer and dvd:
            if dvd in customer.rented_dvds:
                return f'{customer.name} has already rented {dvd.name}'
            if dvd.is_rented:
                return 'DVD is already rented'
            if customer.age < dvd.age_restriction:
                return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
            dvd.is_rented = True
            customer.rented_dvds.append(dvd)
            return f'{customer.name} has successfully rented {dvd.name}'
        return ''

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer: Union[Customer, None] = self.__find_customer_by_id(customer_id=customer_id)
        dvd: Union[DVD, None] = self.__find_dvd_by_id(dvd_id=dvd_id)
        if customer and dvd:
            if dvd in customer.rented_dvds:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f'{customer.name} has successfully returned {dvd.name}'
            return f'{customer.name} does not have that DVD'
        return ''

    def __repr__(self) -> str:
        result_lines: list[str] = [repr(customer) for customer in self.customers]
        result_lines.extend(repr(dvd) for dvd in self.dvds)
        return '\n'.join(result_lines)

    def __find_customer_by_id(self, customer_id: int) -> Union[Customer, None]:
        found_customers: list[Customer] = [customer for customer in self.customers if customer.id == customer_id]
        if found_customers:
            return found_customers[0]
        return None

    def __find_dvd_by_id(self, dvd_id: int) -> Union[DVD, None]:
        found_dvds: list[DVD] = [dvd for dvd in self.dvds if dvd.id == dvd_id]
        if found_dvds:
            return found_dvds[0]
        return None


if __name__ == '__main__':
    # movie_world_instance = MovieWorld(name='The Best Movie Shop')
    pass
