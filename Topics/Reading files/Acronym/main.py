# read test.txt
with open("test.txt", "r") as file_descriptor:
    for line in file_descriptor:
        print(line[0])
file_descriptor.close()
