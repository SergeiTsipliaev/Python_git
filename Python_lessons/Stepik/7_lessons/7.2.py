
m = int(input())
p = int(input())
n = int(input())

population = m

for day in range(0, n):
    print(day + 1, population)
    population = population  + (population * p / 100)



# m = int(input())
# n = int(input())



# for num in range(m, n + 1, +1):
#     if num  % 17 == 0 or num % 10 == 9 or (num % 3 + num % 5 == 0 ):
#         print(num)
    


# n = int(input())



# for num in range(1, 11):
#         print(n, 'x', num, '=', num * n)