count = 50
while True:
    coins = 5, 10, 25
    prompt = int(input(f'Amount due: {count}\nInsert coin: '))
    for coin in coins:
        if prompt == coin:
            count -= prompt
        else:
            pass
    
    if count == 0:
        print(f'Change owed: {count}')
        break
    elif count < 0:
        print(f'Change owed: {abs(count)}')
        break

# count = 50 

# coins = 5, 15, 25

# prompt = int(input("Amount: "))

# for coin in coins:
#     if prompt == coin:
#         count -= prompt



'''
amount due and insert coin
input coin (25c, 10c, 5c) return amount due / owed and insert / break
keep a count of how much is remaining (one bottle is 50c)
if amount paid goes into the negatives we want amount owed

'''