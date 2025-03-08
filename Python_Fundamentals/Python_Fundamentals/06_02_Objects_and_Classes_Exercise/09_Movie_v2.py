class Movie:
    """Represents a movie with attributes for name, director, and watched status."""

    __watched_movies: int = 0

    def __init__(self, name: str, director: str) -> None:
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str) -> None:
        self.name = new_name

    def change_director(self, new_director: str) -> None:
        self.director = new_director

    def watch(self) -> None:
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self) -> str:
        return (
            f'Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}'
        )

# if __name__ == '__main__':
#     movie_1 = Movie(name='Inception', director='Christopher Nolan')
#     movie_2 = Movie(name='Interstellar', director='Christopher Nolan')
#
#     movie_1.watch()
#     movie_2.watch()
#     movie_2.watch()
#
#     print(movie_1)
#     print(movie_2)
