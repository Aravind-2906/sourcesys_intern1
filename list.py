#find second largest number

num=[10, 20, 4, 45, 99]
num.sort()
print("Second Largest:", num[-2])


#remove duplicates
num=[1,2,2,3,5,6,6,77]
new=[]

for i in num:
    if i not in new:
        new.append(i)

print(new)
