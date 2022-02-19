fname=input("enter the file name ")
try:
    fhand=open(fname)
except:
    print("invalid file name")
count=0
for line in fhand:
    if line.startswith('From '):
        fline=line.split()
        print(fline[1])
        count=count+1
print("There were",count,"lines in the file with From as the first word" )
