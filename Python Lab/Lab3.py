## Question 1

n = int(input("Enter last number : "))
print("Numbers      Squares")
i = 0
while(i<n):
    print("    ",i,"    ",i**2)
    i+=1

## Question 2

n = int(input("Enter a number : "))
org_n = n

sum_digits = 0
while(n>0):
    d = n%10  #To extract the last digit
    sum_digits += d
    n = n//10 #To remove the last digit 
print("Number : ",org_n,"\nSum of digits : ",sum_digits)        

## Question 3

n = int(input("Enter the number of terms of series: "))
l = [0,1,]
i = 2
while(i<n):
    l.append(l[i-1] + l[i-2])
    i+=1
print(f"Fibonacci series of {n} terms : ",l)    

 
## Question 4

n = int(input("Enter a number : "))

print(f"Multiplication table of {n} :")
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


## Imp Question 5

s = input("Enter a string : ")
is_alphanumeric = True

for i in range(len(s)):
    if not(s[i].isalnum()):
        is_alphanumeric = False
        break
        
if(is_alphanumeric):
    print("True")
else:
    print("False")    


## Question 6

s = input("Enter a string : ")
ch = input("Enter a character : ")

count = 0
for i in range(len(s)):
    if(s[i] == ch):
        count+=1
        continue

print(f"Number of occurences of {ch} : {count}")
