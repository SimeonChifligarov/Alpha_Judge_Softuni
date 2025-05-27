class Profile:
    """
    This class is about a user profile with username and password.

    Args:
        username (str): The username of the profile.
        password (str): The password of the profile.
    """

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str) -> None:
        if not 5 <= len(value) <= 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        if len(value) < 8 or not any(char.isupper() for char in value) or not any(char.isdigit() for char in value):
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


if __name__ == '__main__':
    # profile_instance = Profile(username='Username', password='Passw0rd')
    # print(profile_instance)
    pass
