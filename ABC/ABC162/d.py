n = int(input())
s = input()

ans = s.count('R') * s.count('G') * s.count('B')

for i in range(n):
    for j in range(i + 1, n):
        k = 2 * j - i
        # 三個目が範囲内 かつ 三文字違う かつ 距離が同じはダメ
        if k < n and (s[i] != s[j] and s[j] != s[k]
                      and s[i] != s[k]) and j - i == k - j:
            ans -= 1

print(ans)
