l = ["1", "69", "420", "", "66"]

result = []
temp_list =[]

for i in l:
    if i == '':
        result.append(temp_list)
        temp_list = []
    else:
        temp_list.append(i)
result.append(temp_list)

    

result = [2 * i for i in [1, 2, 3]]

def dbl(n):
    return n * 2

nums = [1, 2, 3]
result = map(dbl, nums)

from itertools import groupby

result = [list(g) for k, g in groupby(['1', '2', '3', '', '5'])]

print(result)

data = ['1', '69', '420', '', '66']

groups = [list(group) for _, group in groupby(data, lambda x: x == '') if not _]

print(groups)