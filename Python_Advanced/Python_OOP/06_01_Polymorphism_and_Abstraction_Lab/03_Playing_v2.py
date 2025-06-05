from typing import Any


def start_playing(instance: Any) -> str:
    """
    Call the play method of the given instance.

    Args:
        instance (Any): An object that should have a play() method.

    Returns:
        str: The result of calling play() method.
    """
    if not hasattr(instance, 'play') or not callable(getattr(instance, 'play')):
        return ''
    return instance.play()


if __name__ == '__main__':
    # class Guitar:
    #     def play(self) -> str:
    #         return 'Playing the guitar'
    #
    # class Children:
    #     def play(self) -> str:
    #         return 'Children are playing'
    #
    # guitar = Guitar()
    # children = Children()
    #
    # print(start_playing(instance=guitar))
    # print(start_playing(instance=children))
    pass
