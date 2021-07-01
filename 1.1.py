a = 1
b = 1
c = 2

d = ((b+c)/a)


print(a, type(a))
print(b, type(b))
print(c, type(c))


print(d, type(d))
d = int(d)
print('')
e = input('What is next number? ')
word = input('Are you sure? ')
e = int(e)
print(" ")

if e == ((c+d)/b):
    print(e,'is correct!')
    word2 = input('Is it easy? ')
    print('')
    f = input('OK, what is next number? ')
    f = int(f)
    if f == int((d+e)/c):
        print(f, 'is correct!')
    else:
        print('You were close...')
        print('The correct number is ', int((d+e)/c))
        print('Guess why!?')

else:
    print('you said "',word,'" but you are wrong...')
    print('The correct answer is ', int((c+d)/b))
    e = int((c+d)/b)
    print('')
    f = input('OK, what is next number? ')
    f = int(f)
    if f == int((d+e)/c):
        print(f, 'is correct!')
    else:
        print('You were close...')
        print('The correct number is ', int((d+e)/c))
        print('Guess why!?')





