import numpy as np
n=(input("Enter Your Full Name: "))
loopcount=int(input("Enter the number of subjects: "))
marks=[]
for i in range(loopcount):
    x=int(input("Enter the marks scored in subject "))
    marks.append(x)
a=int(input("Enter the total marks for each subject: "))
p=np.sum(marks)/(loopcount*a)*100
print("Hello", n, "Your Percentage in", loopcount, "Subjects is ","%.2f" % p,"%" )

if p>60:
    print("Good Job :)")
else:
    print("Study Hard Next time :(")