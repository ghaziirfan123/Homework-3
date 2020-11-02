# My name is Mohammad Ghazi Irfan and my ID is 1626488

numbers = input().split()
result = []

for num in numbers:
    num = int(num)
    if num >= 0:
        result.append(num)

result.sort()
for num in result:
    print(num, end=' ')