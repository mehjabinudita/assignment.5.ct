user_input = input("Please enter string: ")

num_count = 0
upper_count = 0
lower_count = 0
other_count = 0

for char in user_input:
    if char.isdigit():
        num_count += 1
    elif char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    else:
        other_count += 1

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Numbers: {num_count}")
print(f"Other characters: {other_count}")