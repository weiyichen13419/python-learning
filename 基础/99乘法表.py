# x = 1
# y = 1
# while y <= 9:
#     print(x * y, end=' ')
#     y += 1
#     while x <= 9:
#         print(x * y, end=' ')
#     x += 1

# for row in range(1, 10):
#
#    for item in range(1, row + 1):
#
#       print(f'{item}x{row}={item * row}', end='   ')
#    print('')

row=1
while row <=10:
    item = 1
    while item < row:
        print(f'{item}x{row-1}={item * (row-1)}', end='   ')
        item += 1
    row += 1
    print()