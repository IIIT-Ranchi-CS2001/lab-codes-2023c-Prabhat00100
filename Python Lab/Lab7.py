## Question 1

import matplotlib.pyplot as plt

# Data for Madhya Pradesh
mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]

# Data for Rajasthan
rj_parties = ['INC', 'BJP', 'BSP', 'Others']
rj_seats = [69, 115, 2, 13]

mp_percent = [x / sum(mp_seats) * 100 for x in mp_seats]
rj_percent = [x / sum(rj_seats) * 100 for x in rj_seats]

# Pie Charts
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Madhya Pradesh Pie Chart
axs[0].pie(mp_percent, labels=mp_parties, autopct='%1.1f%%', explode=[0.03 if x == max(mp_percent) else 0 for x in mp_percent])
axs[0].set_title('Madhya Pradesh Seat Share')

# Rajasthan Pie Chart
axs[1].pie(rj_percent, labels=rj_parties, autopct='%1.1f%%', explode=[0.02 if x == max(rj_percent) else 0 for x in rj_percent])
axs[1].set_title('Rajasthan Seat Share')

plt.show()

# Bar Chart
x = range(len(mp_parties))  # Same parties in both states
width = 0.4
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([i - width / 2 for i in x], mp_seats, width=width, label='Madhya Pradesh', color='blue')
ax.bar([i + width / 2 for i in x], rj_seats, width=width, label='Rajasthan', color='orange')

# Adding labels and legend
ax.set_xticks(x)
ax.set_xticklabels(mp_parties)
ax.set_xlabel('Parties')
ax.set_ylabel('Seats Won')
ax.set_title('Assembly Elections 2023 Seat Distribution')
ax.legend()
plt.show()

## Question 2
import random
import math
import matplotlib.pyplot as plt

# Helper functions to determine prime and composite numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def classify_numbers(numbers):
    primes = [x for x in numbers if is_prime(x)]
    composites = [x for x in numbers if not is_prime(x) and x > 1]
    return primes, composites

# Input
K = int(input("Enter the number of random numbers (K, minimum 10): "))
N = int(input("Enter the upper limit (N): "))
if K < 10:
    raise ValueError("K must be at least 10.")

# Generate K random numbers within range N
random_numbers = [random.randint(1, N) for _ in range(K)]

# Classify numbers
primes, composites = classify_numbers(random_numbers)

# Compute squares and square roots
prime_squares = [x ** 2 for x in primes]
composite_roots = [math.sqrt(x) for x in composites]

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Prime numbers vs. their squares
axs[0].scatter(primes, prime_squares, color='green', label='Prime Numbers')
axs[0].set_title('Prime Numbers vs. Squares')
axs[0].set_xlabel('Prime Numbers')
axs[0].set_ylabel('Squares')
axs[0].legend()

# Composite numbers vs. their square roots
axs[1].scatter(composites, composite_roots, color='red', label='Composite Numbers')
axs[1].set_title('Composite Numbers vs. Square Roots')
axs[1].set_xlabel('Composite Numbers')
axs[1].set_ylabel('Square Roots')
axs[1].legend()

plt.tight_layout()
plt.show()