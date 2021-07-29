def sum(*args):
    print(f"vashe slovo - {args}")
aa = ['Name','Yesa', 'Age', 29]

a = [0, 1, 2, 3, 4, 5]
print(type(sum(*a)),sum(*a))

def my_sum(a, b):
    return a + b
def my_pow(a):
    return a**2

a = list(map(lambda x: x**2, a))
print(a)