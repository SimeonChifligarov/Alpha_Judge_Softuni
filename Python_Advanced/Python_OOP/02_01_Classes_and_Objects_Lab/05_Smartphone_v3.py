class Smartphone:
    """
    This class is for a smartphone. It can install apps and be turned on/off.

    Args:
        memory (int): The total memory the phone starts with
    """

    def __init__(self, memory: int) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        """
        This method switches the phone on if it's off, or off if it's on.
        """
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int) -> str:
        """
        This method installs an app if the phone is on and has enough memory.

        Args:
            app (str): The name of the app
            app_memory (int): How much memory the app needs

        Returns:
            str: Message about the install action
        """
        if app_memory <= self.memory:
            if self.is_on:
                self.apps.append(app)
                self.memory -= app_memory
                return f'Installing {app}'
            return f'Turn on your phone to install {app}'
        return f'Not enough memory to install {app}'

    def status(self) -> str:
        """
        This method shows how many apps are installed and memory left.

        Returns:
            str: Info about installed apps and memory
        """
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'

    def __str__(self) -> str:
        return self.status()

    def __repr__(self) -> str:
        return f'Smartphone(memory={self.memory!r}, apps={self.apps!r}, is_on={self.is_on!r})'

    # def __repr__(self) -> str:
    #     cls_name = self.__class__.__name__
    #     attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
    #     return f'{cls_name}({attrs})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Smartphone):
            return self.memory == other.memory and self.apps == other.apps and self.is_on == other.is_on
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Smartphone):
            return len(self.apps) > len(other.apps)
        return NotImplemented

# if __name__ == '__main__':
#     phone_memory = 500
#     phone_instance = Smartphone(memory=phone_memory)
#     print(phone_instance.install(app='Maps', app_memory=100))
#     phone_instance.power()
#     print(phone_instance.install(app='Maps', app_memory=100))
#     print(phone_instance.install(app='Camera', app_memory=450))
#     print(phone_instance.install(app='Music', app_memory=200))
#     print(phone_instance.status())
#     print(str(phone_instance))
#     print(repr(phone_instance))
#     another_phone = Smartphone(memory=300)
#     another_phone.power()
#     another_phone.install(app='Notes', app_memory=100)
#     print(phone_instance > another_phone)
