class Registration:
    """
    This class handles user registration to the library system.
    """

    def add_user(self, user: object, library: object) -> str | None:
        """
        This method adds a user if they are not already registered.

        Args:
            user (User): The user to register
            library (Library): The library where the user will be registered

        Returns:
            str | None: Message if user already exists, otherwise None
        """
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f'User with id = {user.user_id} already registered in the library!'

    def remove_user(self, user: object, library: object) -> str | None:
        """
        This method removes a user if they exist in the library.

        Args:
            user (User): The user to remove
            library (Library): The library from which to remove the user

        Returns:
            str | None: Message if user not found, otherwise None
        """
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return 'We could not find such user to remove!'

    def change_username(self, user_id: int, new_username: str, library: object) -> str:
        """
        This method changes a user's username if their ID exists.

        Args:
            user_id (int): The ID of the user
            new_username (str): The new username
            library (Library): The library to check in

        Returns:
            str: Message about success or failure
        """
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username != new_username:
                    if user.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(user.username)
                    user.username = new_username
                    return f'Username successfully changed to: {new_username} for user id: {user_id}'
                return 'Please check again the provided username - it should be different than the username used so far!'
        return f'There is no user with id = {user_id}!'
