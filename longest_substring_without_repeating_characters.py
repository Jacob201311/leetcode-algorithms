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

    """
        !!!recursion too deep
    """
    def __init__(self):
        self.long_len = 0

    def lengthOfLongestSubstring_v2(self, s):
        if(len(s) <= self.long_len):
            return self.long_len
        if(len(s) == 1):
            return 1

        for i in range(1, len(s)):
            if s[i] not in s[:i]:
                self.long_len = i + 1
                if self.long_len == len(s):
                    return self.lengthOfLongestSubstring_v2(s)
            else:
                self.long_len = i if i > self.long_len else self.long_len
                return self.lengthOfLongestSubstring_v2(s[s.find(s[i]) + 1:])


    """
       !!!Time Limit Exceeded
    """
    def lengthOfLongestSubstring_v3(self, s):
        long_len = 0
        char_index_dict = {}
        for i in range(len(s)):
            if char_index_dict.get(s[i]) != None:
                if long_len < len(char_index_dict):
                    long_len = len(char_index_dict)
                for abandon_str in s[:char_index_dict[s[i]] + 1]:
                    if char_index_dict.get(abandon_str) != None and char_index_dict.get(abandon_str) < char_index_dict[s[i]]:
                        char_index_dict.pop(abandon_str)

            char_index_dict[s[i]] = i


        return len(char_index_dict) if len(char_index_dict) > long_len else long_len


if __name__ == "__main__":
    solution =  Solution()
    print(solution.lengthOfLongestSubstring_v3("bpfbhmipx"))

