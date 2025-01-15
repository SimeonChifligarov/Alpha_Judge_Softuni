import os


def count_files(directory):
    """
    Count the number of files in a directory and its subdirectories.

    Args:
        directory (str): The root directory to start the count.

    Returns:
        int: Total number of files.
    """
    total_files = 0

    for root, dirs, files in os.walk(directory):
        total_files += len(files)

    return total_files


if __name__ == '__main__':
    # Get the directory path of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)

    print(f'Starting count from parent directory: {parent_directory}')

    if os.path.exists(parent_directory):
        file_count = count_files(parent_directory)
        print(f'Total number of files in \'{parent_directory}\' and its subdirectories: {file_count}')
    else:
        print('The parent directory does not exist.')
