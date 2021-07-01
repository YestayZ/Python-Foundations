num = int(input('Please, enter an integer:  '))
original_num = num
max = num%10

num = num // 10
while num > 0:
    if num%10 > max:
        max = num%10
    num = num//10

print(type(original_num))
print(f'The biggest digit in number "{original_num:.0f}" is', max)