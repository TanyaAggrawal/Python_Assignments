x=0
y=0
Hrs = input("Enter hours:")
Rph = input("Enter hours per rate:")
try:
    Hrs = float(Hrs)
    Rph = float(Rph)
except:
    print("enter a numeric value")
    quit()
if Hrs<=40 :

    Gpay=Hrs*Rph
    print(Gpay)

else :

    x=Hrs-40
    y=40*Rph
    Gpay=(x*1.5*Rph)+y
    print(Gpay)
