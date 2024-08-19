"""
Given an integer x, return true if x is a palindrome and false otherwise.
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x_str = str(x)
    bool_list = []
    length = len(x_str)
    if len(x_str) % 2 != 0:
        length = len(x_str) - 1
    rng_len = int(length/2)
    for i in range(rng_len):
        if x_str[i] == x_str[-(i+1)]:
            bool_list.append(True)
        else:
            bool_list.append(False)
    if False not in bool_list:
        return True
    else:
        return False


# Examples Tested
print(isPalindrome(-121))
print(isPalindrome(121))
print(isPalindrome(10))
