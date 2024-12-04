## Question 1

s1 = "Maha Bharat"

sub1 = s1.swapcase()
print(sub1)

print(s1.split("B"))     #--> Example of split

sub2 = s1[5:len(s1)]
print(sub2)

sub3 = s1*3
print(sub3)

sub4 = s1.replace("Maha","Mera")
print(sub4)

sub5 = s1+" Mahan"
print(sub5)

## Question 2

s = "Ba Ba Black Sheep"
sub1 = len(s)
print(sub1)

# Finding 'e' using loop
for i in range(len(s)):
    if(s[i]=='e'):
        print("Found,Index : ",i)
        i+=1
        break

# Using built in function 
sub2 = s.find("e")
print(sub2) 
      
count_a = s.count("a")
print(count_a)

for i in range(0,5):                  #Ask what is wrong in this code.
    if(s[i] == 'B'):
        print(s.replace('B','T'))
        i+=1
        break

print(s.replace("B","T",2))      #2 is the count that we want to replace


## Question 3

s = input("Enter any string :")

sub1 = s[::-1]
if(s==sub1):
    print("Palindrome")
else:
    print("Not a palindrome")    
         
## Question 4

name = input("Enter the name of student : ")
roll = int(input("Enter the roll number of student : "))
marks = int(input("Enter the marks obtained in maths : "))

print("Name:",name)
print("Roll Number :",roll)
print("Marks: ",marks)
if(marks >= 90):
    print("Grade Point: 10")
    print("Remark : Outstanding")
elif(90 > marks >= 80):
    print("Grade point: 9")
    print("Remark : Very good")
elif(80 > marks >= 70):
    print("Grade point : 8")
    print("Remark : Good")
elif(70 > marks >= 60):
    print("Grade point : 7")
    print("Remark : Average")
elif(60 > marks >= 50):
    print("Grade point : 6") 
    print("Remark : Pass")
elif(marks < 50):
    print("Grade point : 0") 
    print("Remark : Fail")

## Question 5
import math
a = int(input("Enter first coefficient: "))
b = int(input("Enter second coefficient: "))
c = int(input("Enter third coefficient: "))

d = b**2 - 4*a*c
if(d==0):
    r1 = -b//(2*a)
    print("The roots are :")
    print(r1)
    print(r1)
elif(d>0):
    r1= ((-b + math.sqrt(d))//2*a)
    r2 = ((-b - math.sqrt(d))//2*a)
    print("The roots are :")
    print(r1)
    print(r2)
else:
    r1 = -b / (2 * a)
    r2 = math.sqrt(-d) / (2 * a)

    print("The roots are :")
    print(r1)
    print(r2)




