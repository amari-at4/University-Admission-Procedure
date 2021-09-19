def number_of_chars(n):
    return 1 + (2 * n)


height = int(input())
width = ((height - 1) * 2) + 1
for i in range(height):
    line = "#" * number_of_chars(i)
    print(line.center(width))
