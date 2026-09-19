class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_alphabetical = list(s)
        s_alphabetical.sort()
        t_alphabetical = list(t)
        t_alphabetical.sort()
        return s_alphabetical == t_alphabetical