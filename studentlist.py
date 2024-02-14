#Programme to find the name and marks in percentage 
t=str(input(" Enter Your Name "))
a=float(input(" Enter Ai Marks "))
b=float(input(" Enter Math Marks "))
c=float(input(" Enter Science Marks "))
d=float(input(" Enter Sst Marks "))
e=float(input(" Enter English Marks "))
tm=float(input(" Enter Marks for each "))
brain=(a+b+c+d+e)/(5*tm)*100
print(t, "Your Percentage in this exam was", brain,"%")