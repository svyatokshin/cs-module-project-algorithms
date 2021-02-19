'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    new_arr = []

    # if there is an empty array return 0
    if len(nums) == 0:
        return 0
    else:
        # we want to first loop through the entire array
        for i in range(0, len(nums)-(k-1)):
            # we then want to loop through this same array, establish the 'window' with k
            highest_num = nums[i]
            for j in range(i, i+k):
                # then we want to find the largest value in that range
                if nums[j] > highest_num:
                    highest_num = nums[j]
                    # once we are through that list of values, we want to append that highest value to the new_arr
            new_arr.append(highest_num)
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
