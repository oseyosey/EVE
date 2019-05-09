file=open("test.txt", mode="r", encoding="utf-8")
while True:
    line = file.readline()
    if line:
        print(line)
        line_test;
    else:
        break
file.close()
