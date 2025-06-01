class Room:
    """This class creates a room and allows guests to take or free the room."""

    def __init__(self, number: int, capacity: int) -> None:
        self.number: int = number
        self.capacity: int = capacity
        self.guests: int = 0
        self.is_taken: bool = False

    def take_room(self, people_count: int) -> str | None:
        if self.is_taken or self.capacity < people_count:
            return f'Room number {self.number} cannot be taken'

        self.guests = people_count
        self.is_taken = True

    def free_room(self) -> str | None:
        if not self.is_taken:
            return f'Room number {self.number} is not taken'

        self.guests = 0
        self.is_taken = False


if __name__ == '__main__':
    # room_instance = Room(number=1, capacity=3)
    # print(room_instance.take_room(people_count=2))
    # print(room_instance.free_room())
    pass
