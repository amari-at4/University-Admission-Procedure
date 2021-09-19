# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    print(sum([int(number) for number in line.split()]))
file.close()
