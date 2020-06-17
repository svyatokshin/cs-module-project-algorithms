'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # first case, if there are no zeros, return array and len(arr)
    new_arr = [num for num in arr if num != 0] + \
        [zero for zero in arr if zero == 0]

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
