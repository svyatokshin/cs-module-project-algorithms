'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    empty_arr = []
    # if arr is empty return False

    if len(arr) == 0:
        return False
    # each array has duplicates and 1 solo number
    # find solo number by finding all duplicates
    else:
        # loop through each element in array
        for i in arr:
            # if element is already in array remove it
            if i in empty_arr:
                empty_arr.remove(i)
            # if element is not in array append it in
            else:
                empty_arr.append(i)
            # this will leave the solo number in the array after the for loop ends
            # pop only element in array as result
        return empty_arr.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
