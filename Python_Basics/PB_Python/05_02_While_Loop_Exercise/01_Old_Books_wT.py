# using while True

# # Solution 1
# NO_MORE_BOOKS_COMMAND = 'No More Books'
#
# checked_books = 0
# target_book = input()
#
# is_book_found = False
# while True:
#     command = input()
#     if command == NO_MORE_BOOKS_COMMAND:
#         break
#
#     current_book = command
#     if current_book == target_book:
#         is_book_found = True
#         break
# 
#     checked_books += 1
#
#
# if is_book_found:
#     print(f'You checked {checked_books} books and found it.')
# else:
#     print('The book you search is not here!')
#     print(f'You checked {checked_books} books.')

# Solution 2

book_to_search = input()
book_count = 0

while True:
    book = input()

    if book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {book_count} books.')
        break

    if book == book_to_search:
        print(f'You checked {book_count} books and found it.')
        break
    else:
        book_count += 1
