while True:
    user_input = input("Please enter two words : ")
    
    if user_input.lower() == 'done' or not user_input:
        print("--bye !!")
        
        break
    
    words = user_input.split()
    
    if len(words) == 2:
        word1, word2 = words
        if word1 < word2:
            print(f"{word1} comes first")
        else:
            print(f"{word2} comes first")
    elif len(words) == 1:
        print("Please enter two words: ")
    else:
        print("Please enter two words: ")