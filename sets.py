#common elements between two sets

set1 = {1,2,3,4}
set2 = {3,4,5,6}

common = set()

for i in set1:
    if i in set2:
        common.add(i)

print(common)
