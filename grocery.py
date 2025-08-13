count = 0
list = []
while True:
    try:
        x = input("Item: ").upper()
        list.append(x)
    except EOFError:
        break

list.sort()
name = list[0]
for i in range(len(list)):
    if (name == list[i]):
        count = count + 1
    else:
        print(count, name)
        count = 1
        name = list[i]
print(count, name)