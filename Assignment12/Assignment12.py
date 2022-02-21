fname=input("enter the file name ")
if len(fname) < 1: fname ='mbox-short.txt'
fhand=open(fname)
lst=list()
di=dict()
for line in fhand:
    if line.startswith('From '):
        fline=line.rstrip()
        word=fline.split()
        words=word[5].split(':')
        lst.append(words[0])
for w in lst:
    di[w]=di.get(w,0)+1
lit=list()
#print(sorted([(v,k) for k,v in di.items()]))  #line comprehension
for k,v in sorted(di.items()):
    print(k,v)
