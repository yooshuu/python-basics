f = open("새파일1.txt", 'w')
for i in range(1, 11):
    data = "%d번쨰 줄입니다.\n" % i
    f.write(data)
f.close()