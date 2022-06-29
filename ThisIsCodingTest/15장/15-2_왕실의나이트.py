k = input()

row = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
cnt = 0

x, y = row[k[0]], int(k[1])  # 나이트의 위치

# 동북, 동남, 서북, 서남, 남동, 남서, 북동, 북서
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        cnt += 1

print(cnt)
