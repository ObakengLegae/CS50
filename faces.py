# prompt = input("Write Something: ")
# convert = prompt.replace(":)", "😊")
# print(convert)
def main():
    prompt = input("Write something: ")
    faces = convert(prompt)
    print(faces)


def convert (faces):
    faces = faces.replace(":)", "🙂")
    faces = faces.replace(":(", "☹️")
    return faces

main()