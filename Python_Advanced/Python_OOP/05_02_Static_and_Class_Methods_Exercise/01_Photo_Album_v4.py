import math


class PhotoAlbum:
    """This class helps you create a photo album, add photos, and display them nicely."""

    PAGE_SEPARATION: str = '-' * 11
    PHOTO_MARK: str = '[]'
    MAX_PHOTOS_PER_PAGE: int = 4

    def __init__(self, total_pages: int) -> None:
        self.pages: int = total_pages
        self.photos: list[list[str]] = [[] for _ in range(total_pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        pages_required: int = math.ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE)
        return cls(pages_required)

    def add_photo(self, photo_label: str) -> str:
        if len(self.photos[-1]) >= self.MAX_PHOTOS_PER_PAGE:
            return 'No more free slots'
        for page_index in range(len(self.photos)):
            for slot_index in range(self.MAX_PHOTOS_PER_PAGE):
                if slot_index == len(self.photos[page_index]):
                    self.photos[page_index].append(photo_label)
                    return f'{photo_label} photo added successfully on page {page_index + 1} slot {slot_index + 1}'

    def display(self) -> str:
        output_lines: list[str] = [self.PAGE_SEPARATION]
        for page_photos in self.photos:
            page_display: str = ' '.join(self.PHOTO_MARK for _ in page_photos)
            output_lines.append(page_display)
            output_lines.append(self.PAGE_SEPARATION)
        return '\n'.join(output_lines)

    def __str__(self) -> str:
        return f'PhotoAlbum with {self.pages} pages and {sum(len(page) for page in self.photos)} photos'

    def __repr__(self) -> str:
        return f'PhotoAlbum(pages={self.pages})'


if __name__ == '__main__':
    # album_instance = PhotoAlbum(total_pages=2)
    # print(album_instance.add_photo(photo_label='baby'))
    # print(album_instance.add_photo(photo_label='first grade'))
    # print(album_instance.add_photo(photo_label='eight grade'))
    # print(album_instance.add_photo(photo_label='party with friends'))
    # print(album_instance.photos)
    # print(album_instance.add_photo(photo_label='prom'))
    # print(album_instance.add_photo(photo_label='wedding'))
    # print(album_instance.display())
    pass
