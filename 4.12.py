import random
list1 = [random.randint(0,100) for _ in range(50)]
index_to_delete = []
for i in range(50):
    if list1[i]%2 == 1:
        index_to_delete.append(i)
for i in range(len(index_to_delete)-1,-1,-1):
    list1.pop(index_to_delete[i])
print(list1)