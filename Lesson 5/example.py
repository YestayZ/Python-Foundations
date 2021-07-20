my_f = open("test.txt", "r")
#content = my_f.readlines()
#print(content)
#$content = my_f.readline()
#print(content)

for line in my_f:
    print(line)
    print("fff")


my_f = open("test.txt", "r")
while True:
    contents = my_f.read(1024)
    print(contents)

    if not contents:
        break


my_f = open("test.txt", "w")
my_list = ["he be", 'te te', 'gege']
my_f.writelines(my_list)
my_f = open("test.txt", "r")
info = my_f.readlines()

my_f.close()