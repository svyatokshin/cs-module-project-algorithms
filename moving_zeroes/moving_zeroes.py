'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):

    # loop through each item of input list
    for i in range(len(arr)):  # 0(n)
        x = arr[i]
        # if the item is non-zero
        if x != 0:
            # extract from the list and place at the beginning
            arr = [x] + arr[:i] + arr[i+1:]  # 0(n)
    return arr

    # Your code here
    # first case, if there are no zeros, return array and len(arr)
    # new_arr = [num for num in arr if num != 0] + \
    #     [zero for zero in arr if zero == 0]

    # return new_arr


def moving_zeroes(arr):
    # left pointer at the beginning
    # right pointer at the end

    # loop until left and right pointers meet
    # swap situation:
    # left sees zero and right sees non-zero
    # swap the items
    # increment left
    # decrement right
    # non-swap situation
    # if left sees non-zero
    # increment left
    # if right sees zero
    # decrement right


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
