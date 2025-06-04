class Robot:
    """
    This class represents a basic robot.

    Args:
        name (str): The name of the robot.
    """

    def __init__(self, robot_name: str) -> None:
        self.name = robot_name

    @staticmethod
    def sensors_amount() -> int:
        """
        Get the number of sensors in a basic robot.

        Returns:
            int: Number of sensors.
        """
        return 12


class MedicalRobot(Robot):
    """
    This class represents a medical robot.
    """

    @staticmethod
    def sensors_amount() -> int:
        """
        Get the number of sensors in a medical robot.

        Returns:
            int: Number of sensors.
        """
        return 6


class ChefRobot(Robot):
    """
    This class represents a chef robot.
    """

    @staticmethod
    def sensors_amount() -> int:
        """
        Get the number of sensors in a chef robot.

        Returns:
            int: Number of sensors.
        """
        return 4


class WarRobot(Robot):
    """
    This class represents a war robot.
    """

    @staticmethod
    def sensors_amount() -> int:
        """
        Get the number of sensors in a war robot.

        Returns:
            int: Number of sensors.
        """
        return 12


def number_of_robot_sensors(given_robot: Robot) -> None:
    """
    Print the number of sensors a robot has.

    Args:
        given_robot (Robot): The robot to check.
    """
    if not isinstance(given_robot, Robot):
        return
    print(given_robot.sensors_amount())


if __name__ == '__main__':
    basic_robot_instance = Robot(robot_name='Robo')
    medical_robot_instance = MedicalRobot(robot_name='Da Vinci')
    chef_robot_instance = ChefRobot(robot_name='Moley')
    war_robot_instance = WarRobot(robot_name='Griffin')

    number_of_robot_sensors(given_robot=basic_robot_instance)
    number_of_robot_sensors(given_robot=medical_robot_instance)
    number_of_robot_sensors(given_robot=chef_robot_instance)
    number_of_robot_sensors(given_robot=war_robot_instance)
