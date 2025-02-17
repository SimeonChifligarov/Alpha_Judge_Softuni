# calculate_rectangle_area = lambda width, height: width * height
#
# if __name__ == '__main__':
#     width_input = int(input())
#     height_input = int(input())
#     area = calculate_rectangle_area(width=width_input, height=height_input)
#     print(area)

if __name__ == '__main__':
    width_input = int(input())
    height_input = int(input())
    print((lambda width, height: width * height)(width=width_input, height=height_input))
