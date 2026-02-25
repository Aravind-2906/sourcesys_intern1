#count element in tuple

t = (1,2,3,2,4,2)
count = 0
search = int(input('enter a search element:'))
for i in t:
    if i == search :
        count += 1


print("Count:", count)
