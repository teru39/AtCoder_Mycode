# 30:51
def cal(year):
    return year // 4 - year // 100 + year // 400


a, b = map(int, input().split())
print(cal(b) - cal(a - 1))
