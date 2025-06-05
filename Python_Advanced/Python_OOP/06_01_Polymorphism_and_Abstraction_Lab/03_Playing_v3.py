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


class Playable:
    """
    This class allows any playable object to be called like a function.
    """

    def __init__(self, item: Any) -> None:
        self.item = item

    def __call__(self) -> str:
        return start_playing(instance=self.item)


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
    # playable_guitar = Playable(item=guitar)
    # playable_children = Playable(item=children)
    #
    # print(playable_guitar())
    # print(playable_children())
    pass
