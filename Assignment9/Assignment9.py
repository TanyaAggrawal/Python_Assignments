fname=input("enter the file name")
try:
    fhand=open(fname)
except:
    print("not a valid file name")
words=list()
for line in fhand:
    fline=line.rstrip()
    pieces=fline.split()
    for x in pieces:
        if x not in words:
            words.append(x)
            words.sort()
print(words)
