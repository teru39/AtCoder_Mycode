from collections import deque

k = int(input())
ans = [i for i in range(1, 10)]
cal1 = [str(i) for i in range(1, 10)]
cal = deque(cal1)

cnt = 0
while (1):
    tmp = cal.popleft()
    last = tmp[-1]
    flag = False
    if last == '0':
        tmp1 = tmp + '0'
        tmp2 = tmp + '1'
    elif last == '9':
        tmp1 = tmp + '8'
        tmp2 = tmp + '9'
    else:
        flag = True
        down = tmp + str(int(last) - 1)
        middle = tmp + last
        up = tmp + str(int(last) + 1)

    if flag:
        ans.append(int(down))
        ans.append(int(up))
        ans.append(int(middle))
        cal.append(down)
        cal.append(up)
        cal.append(middle)
        cnt += 3
    else:
        ans.append(int(tmp1))
        ans.append(int(tmp2))
        cal.append(tmp1)
        cal.append(tmp2)
        cnt += 2

    if cnt > 10**6:
        break
ans.sort()
# print(ans)
print(ans[k - 1])
