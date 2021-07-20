with open('text_hw51.txt', 'w') as f_obj:
    while True:
        inputs = str(input('Enter text: '))
        if inputs == "":
            break
        f_obj.write(inputs + '\n')
f_obj = open('text_hw51.txt', "r")
content = f_obj.read()
print('\n' + content)
