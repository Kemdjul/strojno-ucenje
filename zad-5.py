fopen = open("C:/Users/student/Documents/kemal-strojno/lv1/song.txt")
countObj = {}

for line in fopen:
    line.rstrip()
    words = line.split(" ")

    for word in words:
        if word in countObj:
            countObj[word] += 1
        else:
            countObj[word] = 1

for key in countObj:
    print(key + ':' + str(countObj[key]))