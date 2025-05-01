def kwargs_length(**data: str) -> int:
    """
    This function gets keyword arguments and tells how many were given.

    Args:
        data: Any keyword arguments

    Returns:
        The count of keyword arguments
    """
    count = sum([1 for _ in data])
    return count
