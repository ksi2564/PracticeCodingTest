n = int(input())

cnt = 0  # 3이 포함되는 경우의 수 카운트

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # 시간을 문자열로 바꾸어 단순히 붙여버림.
            if '3' in str(h)+str(m)+str(s):
                cnt += 1

print(cnt)
