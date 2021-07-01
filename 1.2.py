time = input('Please, enter time in seconds: ')



sec = int(time)
min = sec // 60
hr = min // 60

print("%02d:%02d:%02d" % (hr, min % 60, sec % 60))
