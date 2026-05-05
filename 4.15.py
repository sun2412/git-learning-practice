#方法一
list = [i for i in range(0,101)]
list1 = []
for i in range(len(list)):
    if list[i] % 2 == 1:
        list1.append(list[i])
result = sum(list1)
print(result)

#方法二
list = [i for i in range(0,101)]
result = sum([i for i in list if i % 2 == 1])
print(result)

#方法三
list = [i for i in range(0,101)]
result = sum(filter(lambda x: x % 2 == 1, list))
print(result)