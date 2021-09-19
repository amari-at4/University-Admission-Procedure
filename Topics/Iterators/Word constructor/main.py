first_string = input()
second_string = input()
composed_string = []
for first_letter, second_letter in zip(first_string, second_string):
    composed_string.append(first_letter)
    composed_string.append(second_letter)
print("".join(composed_string))
