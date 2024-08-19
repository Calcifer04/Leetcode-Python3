"""
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string ""
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    strs_sorted = sorted(strs)
    print(strs_sorted)
    strs_first = strs_sorted[0]
    strs_last = strs_sorted[-1]
    prefix = ''
    for i in range(min(len(strs_first), len(strs_last))):
        if (strs_first[i] != strs_last[i]):
            return prefix
        prefix = prefix + strs_first[i]
    return prefix


# Examples Tested
print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
