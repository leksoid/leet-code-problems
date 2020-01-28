# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def two_sum(list, target):
    for f_index, f_value in enumerate(list):
        for s_index, s_value in enumerate(list[f_index+1:]):
            if (f_value + s_value) == target:
                return [f_index, list.index(s_value)]
    return None

result = two_sum([2,7,11,15], 9)

print(result)