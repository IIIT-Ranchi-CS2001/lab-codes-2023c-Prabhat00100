import math
## Question 1

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

sum = a+b
print("Sum = ",sum)

difference = a-b
print("Difference = ",difference)

product = a*b
print("Product = ",product)

int_quotient = a//b
print("int_quotient = ",int_quotient)

remainder = a%b
print("Remainder = ",remainder)


## Question 2

a = int(input("Enter first side : "))
b = int(input("Enter second side : "))
c = int(input("Enter third side : "))

perimeter = (a+b+c)
s = perimeter//2
area = (s*(s-a)*(s-b)*(s-c))**1//2

print("Perimeter = ",perimeter)
print("Area = ",area)

#Calculating angle opposite to side a
A = math.acos((b**2 + c**2 - a**2)/(2*b*c)) 

#Calculating angle opposite to side b
B = math.acos((a**2 + c**2 - b**2)/(2*a*c))


#Calculating angle opposite to side c
C = math.acos((a**2 + b**2 - c**2)/(2*a*b))

#Convert angles into degrees
A = math.degrees(A)
B = math.degrees(B)
C = math.degrees(C)

print("Angle opposite to side a = ",A)
print("Angle opposite to side b = ",B)
print("Angle opposite to side c = ",C)

## Question 3 

Z1 = complex(input("Enter first impedance : "))
Z2 = complex(input("Enter second impedance : "))

equ_imp = (Z1*Z2)/(Z1+Z2)
print("Equivalent impedance : ",equ_imp)

realpart = (equ_imp.real)
imagpart = (equ_imp.imag)
print("Real part of equivalent impedance : ",realpart)
print("Imaginary part of equivalent impedance : ",imagpart)
