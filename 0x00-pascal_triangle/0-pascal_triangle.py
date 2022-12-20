# #!/usr/bin/python3
# """Pascal Triangle Interview Challenge"""


# def pascal_triangle(n):
#     """returns a list of lists of numbers
#     representing the pascal triangle"""
#     if n <= 0:
#         return []

#     pascal_triangle = [0] * n

#     for i in range(n):
#         # define a row and fill first and last idx with 1
#         new_row = [0] * (i+1)
#         new_row[0] = 1
#         new_row[len(new_row) - 1] = 1

#         for j in range(1, i):
#             if j > 0 and j < len(new_row):
#                 a = pascal_triangle[i - 1][j]
#                 b = pascal_triangle[i - 1][j - 1]
#                 new_row[j] = a + b

#         pascal_triangle[i] = new_row

#     return pascal_triangle

#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
