from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """longestCommonPrefix
        Example 1:
        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        
        Example 2:
        Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
        
        Accepted
        Runtime: 71 ms, faster than 16.42% of Python3 online submissions for Longest Common Prefix.
        Memory Usage: 14 MB, less than 50.32% of Python3 online submissions for Longest Common Prefix.
    """
    if len(strs) == 1:
        return strs[0]
    x = sorted(strs, key=len)
    elem = x[0]
    counter = 0
    count = len(elem)
    result = []

    while count:
        res = []
        for s in x:
            if elem[:count] == s[:count]:
                res.append(elem[:count])
                counter += 1

        if len(result) <= counter and count < len(elem):
            if len(res[0]) > len(result[0]) or len(res) > len(result):
                result.clear()
                result.extend(res)
                if len(result) == len(strs):
                    return result[0]
        else:
            result.extend(res)

        count -= 1
        counter = 0
    if len(result) > 1 and len(result) == len(strs):
        return result[0]
    return ""

print(longest_common_prefix(["flower","flow","flight"]))
