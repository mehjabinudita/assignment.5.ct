while True:
    user_input = input("Please enter string: ")
    
    if user_input.lower() == 'done':
        break

    special_chars = [',', '.', ':', '!', '?']
    cleaned_input = ''.join(char for char in user_input if char not in special_chars)
    cleaned_input = cleaned_input.upper()
    print(f"Processed string: {cleaned_input}")

print("Bye !")