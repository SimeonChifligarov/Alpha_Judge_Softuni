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

# if __name__ == '__main__':
#     phone_memory = 500
#     phone_instance = Smartphone(memory=phone_memory)
#     print(phone_instance.install(app='Maps', app_memory=100))
#     phone_instance.power()
#     print(phone_instance.install(app='Maps', app_memory=100))
#     print(phone_instance.install(app='Camera', app_memory=450))
#     print(phone_instance.install(app='Music', app_memory=200))
#     print(phone_instance.status())
