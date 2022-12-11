# 1. Write a python script to print the first 10 multiples of 5.

r1 =range(5,55,5)
for a in r1:
    print(a)

# 2. Write a python script to print first 10 multiples of N

for a in range(int(input("x"))):
    print(a)

# 3. Write a python script to print first M multiples of N.

for a in range(int(input("x"))*(int(input("x")))):
    print(a)

# 4. Write a python script to print the first 10 multiples of N in reverse order.
for a in range(int(input("x")),0,-1):
    print((a))

# 5. Write a python script to print table of user’s choice
n = int(input('Enter a number : '))

for i in range(n*2-1, 0, -2):
    print(i)


# 6. Write a python script to print first N even natural numbers
n = int(input('Enter a number : '))

for i in range(n):
    print(i*2+2)

# 7. Write a python script to print first N even natural numbers in reverse order
n = int(input('Enter a number : '))

for i in range(n*2,0,-2):
    print(i)

# 8. Write a python script to print squares of first N natural numbers
n = int(input('Enter a number : '))

for i in range(1, n+1):
    print(i**2)

# 9. Write a python script to print cubes of first N natural numbers
n = int(input('Enter a number : '))

for i in range(1, n+1):
    print(i**3)

# 10. Write a python script to print first 10 multiples of N

n = int(input('Enter a number : '))

for i in range(n, n*11, n):
    print(i)