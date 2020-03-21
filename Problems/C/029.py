# 2:26
def dfs(s):
    if len(s) == n:
        print(s)
    else:
        for c in ['a', 'b', 'c']:
            dfs(s + c)


n = int(input())

dfs("")
