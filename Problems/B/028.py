
# coding: utf-8
s = input()
count = [0 for _ in range(6)]
for c in s:
    count[ord(c) - ord('A')] += 1

for i in range(len(count)):
    if i != len(count)-1:
        print(count[i],end=" ")
    else:
        print(count[i])
