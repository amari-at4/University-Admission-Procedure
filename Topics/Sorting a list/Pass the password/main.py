# the following line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
for password_len in [(password, len(password)) for password in sorted(passwords, key=len)]:
    print(password_len[0], password_len[1])
