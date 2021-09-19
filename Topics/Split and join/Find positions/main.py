# put your python code here
number_list = list(map(int, input().split()))
number = int(input())
matched_positions = []
for position, list_number in enumerate(number_list):
    if list_number == number:
        matched_positions.append(str(position))
if matched_positions:
    print(" ".join(matched_positions))
else:
    print("not found")
