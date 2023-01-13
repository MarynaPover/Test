def CountFrequency(my_list):
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count
my_list = [6, 6, 1, 2, 2, 3, 2, 6, 6, 9, 8, 4, 4, 2, 3, 1, 2]
print(CountFrequency(my_list))
print(CountFrequency(my_list).get(9))