"""
Given a roman numeral, convert it to an integer.
"""


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romandict = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}
    total = 0
    i = 0
    while i < len(s):
        char1 = romandict[s[i]]
        if i + 1 < len(s):
            char2 = romandict[s[i+1]]
            if char1 >= char2:
                total += char1
                i += 1
            else:
                total = total + char2 - char1
                i += 2
        else:
            total = total + char1
            i += 1
    return total


# Examples Tested
print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
