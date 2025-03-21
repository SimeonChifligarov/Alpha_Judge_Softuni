# from pathlib import Path
#
#
# def extract_file_info(file_location: str) -> tuple[str, str]:
#     """Extracts file name and extension from the given `file_location`."""
#     file_path = Path(file_location)
#     return file_path.stem, file_path.suffix.lstrip('.')
#
#
# if __name__ == '__main__':
#     file_location_input: str = input().strip()
#
#     file_name, file_extension = extract_file_info(file_location_input)
#
#     print(f'File name: {file_name}')
#     print(f'File extension: {file_extension}')

from pathlib import Path


def extract_file_info(file_location: str) -> tuple[str, str]:
    """Extracts file name and extension from the given `file_location`."""
    file_path = Path(file_location).name
    name, extension = file_path.rsplit('.', maxsplit=1)
    return name, extension


if __name__ == '__main__':
    file_location_input: str = input().strip()

    file_name, file_extension = extract_file_info(file_location_input)

    print(f'File name: {file_name}')
    print(f'File extension: {file_extension}')
