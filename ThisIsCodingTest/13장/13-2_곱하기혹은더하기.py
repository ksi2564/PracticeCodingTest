n = input()
result = 0

for num in n:
    num = int(num)
    result = max(result*num, result+num)

print(result)
