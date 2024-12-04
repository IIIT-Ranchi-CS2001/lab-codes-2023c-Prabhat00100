## Question 1

s = input("Enter a string : ")
words_list = s.split()
pal_words = []
count = 0

for i in range(len(words_list)):
    if(words_list[i][::-1] == words_list[i]):
        pal_words.append(words_list[i])
        count+=1
        continue
    
print(f"Number of palindrome words : {count}")    
print(f"Palindrome words : {pal_words}")

## Question 2

#Creating a list of integers using list comprehension
n = int(input("Enter the number of observations : "))
numbers = [int(input("Enter a number : ")) for _ in range(n)]

#Calculating mean
mean = sum(numbers)/n
print(f"Mean of the list : {mean}")

#Calculating median
numbers.sort()        #For finding median list should be sorted.
if (n%2 != 0):
    median = numbers[n//2]
else:
    median = (numbers[n//2 - 1] + numbers[n//2])/2
print(f"Medain of the list : {median}")

#Calculating mode
# mode = 3*median - 2*mean
# print(f"Mode of the list : {mode}")

# Calculating mode
from collections import Counter
frequency = Counter(numbers)
max_count = max(frequency.values())
mode = [num for num, count in frequency.items() if count == max_count]
print(f"Mode of the list: {mode}")


## Question 3

l1 = ["CS2001", "MA2001", "HS2001"]
l2 = ["Python", "Maths-III", "Mang.Concepts"]
l3 = []
for i in range(len(l1)):
    l3.append(l1[i] + ":" + l2[i])
print(l3)    

# Using list comprehension
l3 = [f"{code}:{name}" for code, name in zip(l1, l2)]
print(l3)

## Question 4

n = int(input("Enter number of singers : "))
m = int(input("Enter number of dancers : "))
singers = {input("Enter singer's name : ") for _ in range(n)}
dancers = {input("Enter dancer's name : ") for _ in range(m)}

#a.
all_artists = singers | dancers
print(f"All artists in the class : {all_artists}")

#b.
all_rounders = singers & dancers
print(f"All rounders of the class : {all_rounders}")

#c.
dan_not_sing = dancers - singers
print(f"Dancers but not singers : {dan_not_sing}")

#d.
sing_not_dan = singers - dancers
print(f"Singers but not dancers : {sing_not_dan}")

#e.
either_sing_dan_not_both = singers ^ dancers
print(f"Either sigers or dancers but not both : {either_sing_dan_not_both}")