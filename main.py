# Ethan Lawrence
# Nov 1 2024
# Range()

# Counting to twenty 
for num in range(1, 21):
    print(num)
else:
    print('')

# One-Million
# for num in range(1, 1000001):
#     print(num)

# Summing a Million
operations = [min, max, sum]
for x in operations:
    print(x(range(1, 1000001)))
else:
    print('')

# print(min(range(1, 1000001)))
# print(max(range(1, 1000001)))
# print(sum(range(1, 1000001)))
    
# Odd numbers
for num in range(1, 21, 2):
    print(num)
else:
    print('')

# Threes
for num in range(3, 31, 3):
    print(num)
else:
    print('')

# Cubes
for num in range(1, 11):
    print(num**3)