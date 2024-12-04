## Question 1

def my_zip(*args, strct=True):
    if strct:
        # Ensure all lists have the same length
        lengths = [len(lst) for lst in args]
        if len(set(lengths)) != 1:
            raise ValueError("All lists must be of the same length when 'strct' is True.")
        return list(zip(*args))
    else:
        # Zip using the minimum length
        min_length = min(len(lst) for lst in args)
        return [tuple(lst[i] for lst in args) for i in range(min_length)]

customer_name = ['Alice', 'Bob', 'Charlie']
customer_id = [101, 102, 103]
shopping_points = [500, 400, 300]

# Strict zipping
print(my_zip(customer_name, customer_id, shopping_points, strct=True))

# Lenient zipping
customer_name = ['Alice', 'Bob']
print(my_zip(customer_name, customer_id, shopping_points, strct=False))

## Question 2
def my_sort(data, key):
    if not data or not isinstance(data[0], tuple):
        raise ValueError("Input data must be a list of tuples.")
    if key not in (0, 1, 2):
        raise ValueError("Key must be 0, 1, or 2.")
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

customer_data = [
    ('Charlie', 103, 300),
    ('Alice', 101, 500),
    ('Bob', 102, 400)
]

# Sort by customer name (key=0)
print(my_sort(customer_data[:], key=0))

# Sort by customer ID (key=1)
print(my_sort(customer_data[:], key=1))

# Sort by shopping points (key=2)
print(my_sort(customer_data[:], key=2))

## Question 3
def my_max(*args):
    if not args:
        raise ValueError("No arguments provided.")
    max_value = args[0]
    for value in args:
        if value > max_value:
            max_value = value
    
    return max_value
# List
numbers_list = [1, 4, 9, 3]
print("Max in list:", my_max(*numbers_list))  

# Set
numbers_set = {5, 8, 12, 7}
print("Max in set:", my_max(*numbers_set)) 

# Tuple
numbers_tuple = (10, 20, 15, 25)
print("Max in tuple:", my_max(*numbers_tuple)) 

## Question 4
input_string = input("Enter a comma-separated string: ")
components = [comp.strip() for comp in input_string.split(',')]

# 1. Find all letters and convert them to uppercase
letters_uppercase = list(
    map(lambda x: x.upper(), filter(lambda x: x.isalpha(), components))
)
print("Uppercase letters:", letters_uppercase)

# 2. Find all digits and compute their squares
digits_squared = list(
    map(lambda x: int(x) ** 2, filter(lambda x: x.isdigit(), components))
)
print("Squared digits:", digits_squared)

# 3. Display all alphanumeric characters
alphanumeric = list(filter(lambda x: x.isalnum(), components))
print("Alphanumeric characters:", alphanumeric)