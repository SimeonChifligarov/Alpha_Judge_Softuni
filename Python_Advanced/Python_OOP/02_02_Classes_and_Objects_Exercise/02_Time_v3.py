class Time:
    """
    This class keeps track of time using hours, minutes, and seconds.

    Args:
        hours (int): The hour value
        minutes (int): The minute value
        seconds (int): The second value
    """

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        """
        This method sets new values for the time.

        Args:
            hours (int): New hour
            minutes (int): New minute
            seconds (int): New second
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        """
        This method returns the time in a readable string format.

        Returns:
            str: Time in "hh:mm:ss" format
        """
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self) -> str:
        """
        This method moves the time one second forward and returns the new time.

        Returns:
            str: Updated time
        """
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return self.get_time()

    def __str__(self) -> str:
        return self.get_time()

    def __repr__(self) -> str:
        return f'Time(hours={self.hours!r}, minutes={self.minutes!r}, seconds={self.seconds!r})'

    # def __repr__(self) -> str:
    #     cls_name = self.__class__.__name__
    #     attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
    #     return f'{cls_name}({attrs})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Time):
            return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Time):
            return (self.hours, self.minutes, self.seconds) > (other.hours, other.minutes, other.seconds)
        return NotImplemented

# if __name__ == '__main__':
#     start_hour = 23
#     start_minute = 59
#     start_second = 58
#     time_instance = Time(hours=start_hour, minutes=start_minute, seconds=start_second)
#     print(time_instance.get_time())
#     print(time_instance.next_second())
#     print(time_instance.next_second())
#     time_instance.set_time(hours=12, minutes=30, seconds=45)
#     print(time_instance.get_time())
#     print(str(time_instance))
#     print(repr(time_instance))
#     another_time = Time(hours=12, minutes=30, seconds=45)
#     print(time_instance == another_time)
#     print(time_instance > Time(hours=10, minutes=0, seconds=0))
