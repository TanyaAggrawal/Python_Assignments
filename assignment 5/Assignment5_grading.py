score = input("Enter Score: ")
try:
    score= float(score)
except:
    print("Enter a numeric value between 0.0 and 1.0")
    quit()

if score>1.0:
    print("value not between 0.0 ans 1.0")
    quit()

elif score>=0.9:
    print("A")

elif score>=0.8:
    print("B")

elif score>=0.7:
    print("C")

elif score>=0.6:
    print("D")

elif score>0.6:
    print("E")





        
