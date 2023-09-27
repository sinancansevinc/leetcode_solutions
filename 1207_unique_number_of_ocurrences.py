def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    if (len(set(arr)) == len(arr)):
        return False
    arr_dict = {}
    for i in arr:
        if i in arr_dict:
            arr_dict[i] += 1
        else:
            arr_dict[i] = 1

    return len(set(arr_dict.values())) == len(arr_dict.values())


print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
