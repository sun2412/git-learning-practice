import random
list1 = [random.randint(0, 100) for _ in range(20)]
print("原始列表:", list1)
even_index_elements = [list1[i] for i in range(0, len(list1), 2)]
even_index_elements.sort(reverse=True)
index = 0
for i in range(0, len(list1), 2):
    list1[i] = even_index_elements[index]
    index += 1
print("处理后的列表:", list1)