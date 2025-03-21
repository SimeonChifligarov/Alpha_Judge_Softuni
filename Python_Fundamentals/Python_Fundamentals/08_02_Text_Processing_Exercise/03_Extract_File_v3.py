def extract_file_details(file_path: str) -> tuple[str, str]:
    """
    Extracts the file name and its extension from the given file path.
    Returns a tuple containing (file_name, file_extension).
    """
    file_name_with_ext: str = file_path.split('\\')[-1]
    file_name, file_extension = file_name_with_ext.rsplit('.', maxsplit=1)
    return file_name, file_extension


if __name__ == '__main__':
    file_path_input: str = input()
    file_name_result, file_extension_result = extract_file_details(file_path=file_path_input)
    print(f'File name: {file_name_result}')
    print(f'File extension: {file_extension_result}')
