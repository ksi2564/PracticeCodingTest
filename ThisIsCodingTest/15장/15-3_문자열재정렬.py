s = input()
s_list = []  # 알파벳만 담을 리스트
value = 0  # 숫자를 모두 더한 값
cnt = 0  # 숫자를 몇 번 더했는지 체크

for n in s:
    if n.isalpha():
        s_list.append(n)
    else:
        value += int(n)
        cnt += 1

# 알파벳 오름차순 정렬
s_list.sort()

if cnt != 0:
    s_list.append(str(value))

# 리스트를 문자열로 변환하여 출력
print(''.join(s_list))
