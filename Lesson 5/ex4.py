file = []
with open("python.txt", "w") as f_obj:
    import os

    content = os.listdir(path=".")
    print(content)
