fname=input("enter the name of the file ")
if len(fname) < 1: fname = 'mbox-short.txt'
fhand=open(fname)
lst=list()
di=dict()
for line in fhand:
    if line.startswith('From '):
        fline=line.split()
        lst.append(fline[1])
for word in lst:
    di[word]=di.get(word,0)+1
grno=None
grwo=None
for key,val in di.items():
    if grno == None or val > grno:
        grno=val
        grwo=key
print(grwo,grno)
