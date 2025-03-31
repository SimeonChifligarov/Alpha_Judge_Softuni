import re

pattern = r'((?<= _)|(?<=^_))[a-zA-Z0-9]+\b'

line_data = input()
var_names = [el.group() for el in re.finditer(pattern, line_data)]

print(*var_names, sep=',')
