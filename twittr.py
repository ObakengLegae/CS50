prompt = input("Input text: ")

vowels = ['a', 'e', 'i', 'o', 'u']
for i in prompt:
    empty = []
    new = []
    if i.lower() in vowels:
        empty.append(i)
    else:
        new.append(i)
    
    new_word = "".join(new)
    print(new_word, end="")