import numpy as np
n=input("Enter Your Full Name: ")
loopcount =int(input("enter the no. of subjects :"))
marks =[]
for i in range(loopcount):
    x= int(input("enter the mark scored in subject :"))
    marks.append(x)
a=int(input("Total Marks for each subject: "))
p=float(np.sum(marks)/(loopcount*a)*100)

print("Hello", n, "Your Percentage in", loopcount, "Subjects is ","%.2f" % p,"%" )

'''for x in marks:
    print(x) '''
