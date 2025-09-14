def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row in range(2, n):
        new_row = [1]
        for col in range(1, row):
            new_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
