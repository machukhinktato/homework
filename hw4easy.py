# exercise 1

# v.1
# main_list = []
# unknown_list = []
# for x in range (10):
#     main_list.append(x)
# for i in main_list.copy():
#     k = i ** 2
#     unknown_list.append(k)
# print(main_list)
# print(unknown_list)

# v.2
list1 = [-1, 2, 3, 4, 5, 6, 7, -4]
list2 = [i ** 2 for i in list1]
print(list2)

# exercise 2

# v.1
# fruit_list = ['дыня', 'яблоко', 'мандарин', 'манго', 'груша', 'апельсин', 'нектарин']
# fruit_list_v2 = ['банан', 'киви', 'яблоко', 'лимон', 'груша', 'ананас', 'мандарин', 'мангустин', 'дыня']
# united_fruit_list = list(set(fruit_list) & set(fruit_list_v2))
# print(united_fruit_list)

# v.2
fruits_list_1 = ['дыня', 'яблоко', 'мандарин', 'манго', 'груша', 'апельсин', 'нектарин']
fruits_list_2 = ['банан', 'киви', 'яблоко', 'лимон', 'груша', 'ананас', 'мандарин', 'мангустин', 'дыня']

fruits_list_3 = [i for i in fruits_list_1 if i in fruits_list_2]
print(fruits_list_3)

# exercise 3

list3 = [1, 2, 3, 4, 5, 6, 7, 8, -4, -5, -3, 12, 27]
list4 = [i for i in list3 if i % 3 == 0 and i > 0 and i % 4 != 0]
print(list4)
