Words = str(input('Enter a text:   '))
commas = Words.split()
print()
n = 1
for i in commas:
    print(f"{n}. {i[:10]}")
    n = n + 1
