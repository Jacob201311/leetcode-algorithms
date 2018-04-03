"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:


    """
	232ms
	>26.85
	https://leetcode.com/submissions/detail/148322142/
    """
    def lengthOfLongestSubstring_v1(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str = []
        result = {}
        flag = True
        for x in s:
            temp = []
            for sub in sub_str:
                temp.append(sub)
                if x == sub:
                    if result and result[0] < len(sub_str):
                        result[0] = len(sub_str)
                    elif not result:
                        result[0] = len(sub_str)

                    sub_str = [str_temp for str_temp in "".join(sub_str).replace("".join(temp), "")]
                    sub_str.append(x)
                    flag = False
                    break

            if flag:
                sub_str.append(x)
            flag = True


        if not result:
            if sub_str:
                return len(sub_str)
            else:
                return 0
        else:
            return result[0] if result[0] > len(sub_str) else len(sub_str)

if __name__ == "__main__":
    solution =  Solution()
    print(solution.lengthOfLongestSubstring_v1("bpfbhmipx"))

