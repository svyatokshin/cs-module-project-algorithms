'''
Input: an integer
Returns: an integer
'''


# def eating_cookies(n):
#     # first set up known return amounts for n
#     if n <= 1:
#         return 1
#         # getting to a negative number means we didnt find one of the ways
#     elif n == 2:
#         return 2
#     # using recursion you can figure out the amount of cookies eaten
#     # we know that
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache=None):
    # Your code here
    if n < 0:
        return 0

    if n == 0:
        return 1

    if n == 1:
        return 1

    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    cache[n] = eating_cookies(
        n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    return cache[n]


print(eating_cookies(5))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
