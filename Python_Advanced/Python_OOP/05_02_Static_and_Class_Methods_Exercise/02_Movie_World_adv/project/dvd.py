class DVD:
    """This class helps to create a DVD that can be rented by customers."""

    MONTHS: dict[int, str] = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December',
    }

    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name: str = name
        self.id: int = dvd_id
        self.creation_year: int = creation_year
        self.creation_month: str = creation_month
        self.age_restriction: int = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date_str: str, age_restriction: int) -> 'DVD':
        _, month, year = [int(part) for part in date_str.split('.')]
        month_name: str = cls.MONTHS.get(month, '')
        return cls(name=name, dvd_id=dvd_id, creation_year=year, creation_month=month_name, age_restriction=age_restriction)

    def __repr__(self) -> str:
        status: str = 'rented' if self.is_rented else 'not rented'
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}'


if __name__ == '__main__':
    # dvd_instance = DVD(name='Black Widow', dvd_id=1, creation_year=2020, creation_month='April', age_restriction=18)
    pass
