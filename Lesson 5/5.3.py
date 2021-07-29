a = [x.rstrip().split() for x in open("text_hw53.txt", "r") if x.rstrip()]
low_than_20 = []
for items in a:
    if int(items[1]) < 20000:
        low_than_20.append(items[0])
print(f"\n{', '.join(low_than_20)} earn below than 20000")
i = 0
mid = []
while i < len(a):
    mid.append(int(a[i][1]))
    i += 1
mid = sum(mid) / len(mid)
print(f"Average employees income = {round(mid, 2)}")