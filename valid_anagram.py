class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dict_s = {}
            dict_t = {}
            for i in s:  # O(n)
                dict_s[i] = dict_s.get(i, 0) + 1
            for i in t:  # O(n)
                dict_t[i] = dict_t.get(i, 0) + 1

            return dict_s == dict_t  # O(n)

        return False
