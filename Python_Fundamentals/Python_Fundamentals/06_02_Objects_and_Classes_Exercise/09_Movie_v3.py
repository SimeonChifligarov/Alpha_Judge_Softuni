class Movie:
    __watched_movies = 0

    def __init__(self, name: str, director: str):
        """Initializes the movie with a name, director, and a default watched status of False."""
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):
        """Changes the name of the movie."""
        self.name = new_name

    def change_director(self, new_director: str):
        """Changes the director of the movie."""
        self.director = new_director

    def watch(self):
        """Marks the movie as watched and increments the class-level counter."""
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self) -> str:
        """Returns a formatted string representation of the movie."""
        return f'Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}'  # noqa
