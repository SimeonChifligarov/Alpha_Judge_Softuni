from typing import Union
from project.room import Room


class Hotel:
    """This class helps to create a hotel and manage its rooms and guests."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rooms: list[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> 'Hotel':
        hotel_name: str = f'{stars_count} stars Hotel'
        return cls(hotel_name)

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people_count: int) -> None:
        room_instance: Union[Room, None] = self.__find_room_by_number(room_number=room_number)
        if room_instance:
            take_result: Union[str, None] = room_instance.take_room(people_count=people_count)
            if take_result is None:
                self.guests += people_count

    def free_room(self, room_number: int) -> None:
        room_instance: Union[Room, None] = self.__find_room_by_number(room_number=room_number)
        if room_instance:
            if room_instance.is_taken:
                self.guests -= room_instance.guests
                room_instance.free_room()

    def status(self) -> str:
        free_rooms_list: list[str] = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms_list: list[str] = [str(room.number) for room in self.rooms if room.is_taken]
        return (
            f'Hotel {self.name} has {self.guests} total guests\n'
            f'Free rooms: {", ".join(free_rooms_list)}\n'
            f'Taken rooms: {", ".join(taken_rooms_list)}'
        )

    def __find_room_by_number(self, room_number: int) -> Union[Room, None]:
        found_rooms: list[Room] = [room for room in self.rooms if room.number == room_number]
        if found_rooms:
            return found_rooms[0]
        return None


if __name__ == '__main__':
    # hotel_instance = Hotel.from_stars(stars_count=5)
    # room_1 = Room(number=1, capacity=3)
    # room_2 = Room(number=2, capacity=2)
    # room_3 = Room(number=3, capacity=1)
    # hotel_instance.add_room(room=room_1)
    # hotel_instance.add_room(room=room_2)
    # hotel_instance.add_room(room=room_3)
    # hotel_instance.take_room(room_number=1, people_count=4)
    # hotel_instance.take_room(room_number=1, people_count=2)
    # hotel_instance.take_room(room_number=3, people_count=1)
    # hotel_instance.take_room(room_number=3, people_count=1)
    # print(hotel_instance.status())
    pass
