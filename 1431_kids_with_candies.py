# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]

def kidsWithCandies(candies: list, extraCandies: int) -> list:
    boolean_array = []

    for i in range(len(candies)):
        if candies[i]+extraCandies >= max(candies):
            boolean_array.append(True)
        else:
            boolean_array.append(False)

    return boolean_array


# print(kidsWithCandies([2, 3, 5, 1, 3], 3))

print(kidsWithCandies([12, 1, 12], 10))
