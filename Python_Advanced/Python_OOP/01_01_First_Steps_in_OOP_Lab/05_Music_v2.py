class Music:
    """
    Represent a music track with title, artist, and lyrics.

    Args:
        title: the title of the song
        artist: the performer of the song
        lyrics: the full lyrics of the song
    """

    def __init__(self, title: str, artist: str, lyrics: str) -> None:
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self) -> str:
        """
        Return information about the song.

        Returns:
            A string showing title and artist
        """
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self) -> str:
        """
        Return the lyrics of the song.

        Returns:
            The lyrics string
        """
        return self.lyrics
