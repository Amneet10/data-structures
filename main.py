
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28,21,27,31]
l3 = []
for i in l1:
    if (i  % 2 ) != 0:
        l3.append(i)
for i in l2:
    if(i % 2)== 0:
        l3.append(i)

print(l3)