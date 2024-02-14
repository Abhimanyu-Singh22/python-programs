import datetime
# print current date and time 

now=datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%Y-%m"))

# print leap  year ()
x=int(input(" Enter the year to check leap year "))
#y=x%4
if x%4==0:
    print("it is a leap year ")
else:
    print(" It is not a leap year ")

#print a table of a number
x=int(input("Enter the number for its table "))
for i in range(10):
    print((i+1)*x)
 
#print pyramid for number of rows
row=int(input(" ENter the no. of rows "))
for i in range(row):
    for j in range(i+1):
        print(i, end="")
    print("\n")



#find the length of input and reverse the string 
strinput=input(" Enter the String ")
print("The Lenght of "+ strinput +" is" , len(strinput))

str1=""

for i in strinput:
    str1= i+str1
print(str1)

print(strinput.replace("a", "1"))
print(strinput[::-1])
print(strinput[-3:])


x=("applle", "banan")
print(x[:])