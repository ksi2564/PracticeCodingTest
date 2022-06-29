n = int(input())  # 모험가 수
x = list(map(int, input().split()))  # 공포도

x.sort()

result = 0  # 결성된 그룹의 수
cnt = 0  # 현재 그룹에 포함된 모험가의 수

for i in x:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)
