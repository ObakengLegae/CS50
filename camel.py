def main():
    prompt = input('camelCase: ')
    print(f'snake_case: {convert(prompt)}')

def convert(prompt):
    empty_list = []

    for char in prompt:
        if char.islower():
            empty_list.append(char)
        else:
            empty_list.append("_")
            empty_list.append(char)


    new_word = "".join(empty_list).lower()

    return new_word

main()