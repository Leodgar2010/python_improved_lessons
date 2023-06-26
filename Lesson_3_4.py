# arr = [2, 2, 5, 6, 7, 8, 3, 4, 5, 6, 1, 3, 4, 9, 8, 7, 6, 5]
# for i in arr:
#     if arr.count(i) == 2:
#         arr = list(filter(lambda a: a != i, arr))
# print(arr)
COUNT=2
arr2 = [2, 2, 5, 6, 7, 8, 3, 4, 5, 6, 1, 3, 4, 9, 8, 7, 6, 5]
for i in set(arr2):
    if arr2.count(i) == COUNT:
        for k in range(COUNT):
            arr2.remove(i)
print(arr2)

# from collections import Counter
#
# my_list = [2,2,5,6,7,8,3,4,5,6,1,3,4,9,8,7,6,5]
# unique_list = list(Counter(my_list))
#
# print(unique_list)
