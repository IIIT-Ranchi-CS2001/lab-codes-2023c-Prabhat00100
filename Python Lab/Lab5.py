## Question 1
import math

x1 = float(input("Enter x1 coordinate : "))
y1 = float(input("Enter y1 coordinate : "))
z1 = float(input("Enter z1 coordinate : "))
point1 = (x1,y1,z1)

x2 = float(input("Enter x2 coordinate : "))
y2 = float(input("Enter y2 coordinate : "))
z2 = float(input("Enter z3 coordinate : "))
point2 = (x2,y2,z2)

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(f"Euclidean distance between two points : {distance}")

## HW From Tuple notes 

students = ("Bibek", "Pahul", "Yugraj", "Sonny", "Parnab")
marks = (67, 82, 91, 55, 78)

zip_result = zip(students, marks)  #zip() function only zips.
result = tuple(zip_result)         #Combined students and marks into a tuple. 
print(result)          

# Sorting by marks using lambda() function. 
l = list(result)
l.sort(key=lambda x:x[1])
print(l)



## Question 2

x1 = float(input("Enter x1 coordinate : "))
y1 = float(input("Enter y1 coordinate : "))
point1 = (x1,y1)

x2 = float(input("Enter x2 coordinate : "))
y2 = float(input("Enter y2 coordinate : "))
point2 = (x2,y2)

#For slope 
m = (y2-y1)/(x2-x1)
#For y-intercept
c = y1-(m*x1)

# Equation of straight line passing through these points 
print(f"The required equation of point ({x1,y1} and {x2,y2}) is :  y = {m}x + {c}")

## Practice question from dictionary notes (Students grade dictionary)

# dict1 = {
#     "Utkarsh" : 91,
#     "Prabhat" : 95,
#     "Rishi" : 99,
#     "Suraj" : 100,
#     "Ayush" : 92
# }

# dict1.update({"Jay" : 94})
# print("After adding new student : ",dict1)

# dict1["Prabhat"] = 96
# print("After changing one student's grade : ",dict1)

# dict1.pop("Utkarsh")
# print("After removing one student : ",dict1)

# a = max(dict1, key = dict1.get)
# print(a, dict1[a])

# l = dict1.values()
# avg = sum(l)/len(l)
# print(f"Average of grades : {avg}")

# print(f"Final dictionary : {dict1}")

##Imp Question 3

# Function to count the number of each character in a string

def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = input("Enter a string : ")
character_count = count_characters(input_string)   
print("Character count : ",character_count)         

## Question 4
n = int(input("Enter the numbers of customers : "))

customer_name = [input(f"Enter name of customer {i+1}  : ") for i in range(n)]
customer_id = [input(f"Enter id of customer {i+1} : ") for i in range(n)]
shopping_points = [input(f"Enter points of customer {i+1} : ") for i in range(n)]

# Using zip function

customer_list = list(zip(customer_name,customer_id,shopping_points))
print("List with zip function : ",customer_list)

# Without using zip function

customer_list = [(customer_name[i],customer_id[i],shopping_points[i]) for i in range(n)]
print("List without zip function : ",customer_list)

## Question 5

#Using sorted function 
sorted_customer = sorted(customer_list, key = lambda x:x[1])   # x:x[1] is for sorting by second element in list (customer id in this case )
print("Sorted list : ",sorted_customer)

#Without using sorted function

for i in range(n):
    if customer_list[i][1] > customer_list[i+1][1]:
        customer_list[i],customer_list[i+1] = customer_list[i+1],customer_list[i]
    
print(customer_list)        
        

