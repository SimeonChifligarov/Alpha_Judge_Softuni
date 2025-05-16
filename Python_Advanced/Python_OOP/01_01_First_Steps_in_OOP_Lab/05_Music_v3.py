class Music:
    """
    Represent a music track with title, artist, and lyrics.

    Args:
        title: the name of the song
        artist: the performer of the song
        lyrics: the lyrics of the song
    """

    def __init__(self, title: str, artist: str, lyrics: str) -> None:
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self) -> str:
        """
        Return basic song info.

        Returns:
            Title and artist as string
        """
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self) -> str:
        """
        Return the lyrics of the song.

        Returns:
            Lyrics as a string
        """
        return self.lyrics

    def __str__(self) -> str:
        return self.print_info()

    def __repr__(self) -> str:
        return f'Music(title={self.title!r}, artist={self.artist!r}, lyrics={self.lyrics!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Music):
            return False
        return self.title == other.title and self.artist == other.artist and self.lyrics == other.lyrics

    def __len__(self) -> int:
        """
        Return the number of characters in the lyrics.

        Returns:
            Integer character count
        """
        return len(self.lyrics)

    def __hash__(self) -> int:
        return hash((self.title, self.artist, self.lyrics))
