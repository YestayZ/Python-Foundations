a_list = [3, 4, 3, 4, 5, 5, 4]
b_list = ["Jenny", "Bob", "Stuart", "Alice", "Germiona", "Smith", "Ben"]
c_list = ["Requires attention", "Performs good", "Exceeds expectations"]

final_list = dict(zip(b_list,a_list))


print(a_list, ":", type(a_list))
print(b_list, ":", type(b_list))
print(c_list, ":", type(c_list))
print(final_list, ":", type(final_list))
print()
d_list = []
f = []
for i in range(0, 6):
    if a_list[i] == 3:
        d_list.append(c_list[0])
    elif a_list[i] == 4:
        d_list.append(c_list[1])
    elif a_list[i] == 5:
        d_list.append(c_list[2])
    else:
        import sys
        sys.exit()

for i in range(0, 6):
    print(f'{b_list[i]} scored {a_list[i]}. {d_list[i]}.')

