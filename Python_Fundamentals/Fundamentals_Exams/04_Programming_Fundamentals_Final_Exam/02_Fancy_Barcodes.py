# import re
#
# n = int(input())
#
# pattern = re.compile(r'^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$')
# for _ in range(n):
#     s = input()
#     m = pattern.match(s)
#     if not m:
#         print("Invalid barcode")
#         continue
#     core = m.group(1)
#     digits = ''.join(ch for ch in core if ch.isdigit())
#
#     print(f"Product group: {digits if digits else '00'}")

import re

n = int(input())
for _ in range(n):
    barcode = input()
    match = re.match(r'^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$', barcode)
    if not match:
        print("Invalid barcode")
    else:
        core = match.group(1)
        digits = "".join(ch for ch in core if ch.isdigit())
        print(f"Product group: {digits if digits else '00'}")
