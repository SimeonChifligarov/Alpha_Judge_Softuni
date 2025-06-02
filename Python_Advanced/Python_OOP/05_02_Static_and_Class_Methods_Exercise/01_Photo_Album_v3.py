class PhotoAlbum:
    """This class helps to create a photo album with pages and add photos to it."""

    PHOTOS_PER_PAGE: int = 4

    def __init__(self, pages: int) -> None:
        self.pages: int = pages
        self.photos: list[list[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        needed_pages: int = (photos_count + cls.PHOTOS_PER_PAGE - 1) // cls.PHOTOS_PER_PAGE
        return cls(needed_pages)

    def add_photo(self, label: str) -> str:
        for page_index, page_photos in enumerate(self.photos):
            if len(page_photos) < self.PHOTOS_PER_PAGE:
                page_photos.append(label)
                return f'{label} photo added successfully on page {page_index + 1} slot {len(page_photos)}'
        return 'No more free slots'

    def display(self) -> str:
        result_lines: list[str] = []
        for page_photos in self.photos:
            result_lines.append('-' * 11)
            if page_photos:
                result_lines.append(' '.join('[]' for _ in page_photos))
            else:
                result_lines.append('')
        result_lines.append('-' * 11)
        return '\n'.join(result_lines)

    def __str__(self) -> str:
        return f'PhotoAlbum with {self.pages} pages'

    def __repr__(self) -> str:
        return f'PhotoAlbum(pages={self.pages})'


if __name__ == '__main__':
    # album_instance = PhotoAlbum(pages=2)
    # print(album_instance.add_photo(label='baby'))
    # print(album_instance.add_photo(label='first grade'))
    # print(album_instance.add_photo(label='eight grade'))
    # print(album_instance.add_photo(label='party with friends'))
    # print(album_instance.photos)
    # print(album_instance.add_photo(label='prom'))
    # print(album_instance.add_photo(label='wedding'))
    # print(album_instance.display())
    pass
