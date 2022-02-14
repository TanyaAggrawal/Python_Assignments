fname=input("enter file name",)
try:
    fhand=open(fname)

except:
    print("enter a valid file name")
data=0
count=0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        fline=line.rstrip()
        fline=fline[20:27]
        fline=float(fline)
        data=fline+data
print("Average spam confidence:",data/count)
