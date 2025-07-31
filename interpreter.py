numbers = (input('''
+ to add
- to subtract
* to multiply 
/ to divide
example: 2 + 2
                 
Enter Expression: '''))
calculate = float(eval(numbers))
print(calculate)