fname=input("enter the name")
fhand=open(fname)

for line in fhand:
    fline=line.rstrip()
    print (fline.upper())
