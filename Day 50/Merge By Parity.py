https://my.newtonschool.co/playground/code/72tfozosxwq0


n, m = map(int, input().split())
v = list(map(int, input().split()))
x = list(map(int, input().split()))
even = []
odd = []
i = 0
j = 0
while i < n and j < m:
    if v[i] % 2 == 0 and x[j] % 2 == 0:
        if v[i] > x[j]:
            even.append(x[j])
            j += 1
        else:
            even.append(v[i])
            i += 1
    elif v[i] % 2 == 1 and x[j] % 2 == 1:
        if v[i] > x[j]:
            odd.append(x[j])
            j += 1
        else:
            odd.append(v[i])
            i += 1
    elif v[i] < x[j]:
        if v[i] % 2:
            odd.append(v[i])
            i += 1
        else:
            even.append(v[i])
            i += 1
    else:
        if x[j] % 2:
            odd.append(x[j])
            j += 1
        else:
            even.append(x[j])
            j += 1
while i < n:
    if v[i] % 2:
        odd.append(v[i])
        i += 1
    else:
        even.append(v[i])
        i += 1
while j < m:
    if x[j] % 2:
        odd.append(x[j])
        j += 1
    else:
        even.append(x[j])
        j += 1
for i in even:
    print(i, end=" ")
for i in odd:
    print(i, end=" ")
