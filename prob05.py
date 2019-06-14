# 문제 5.

l = [5, 9, 3, 8, 60, 20, 1]

print('Before sort.')
print(l)

change_count = 0
while change_count == 0:
    change_count = -1
    for x in range(0, len(l)-1):
        if l[x] < l[x+1]:
            temp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = temp
            change_count = 0


print('After sort.')
print(l)

