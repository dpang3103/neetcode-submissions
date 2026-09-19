from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            check_str = "".join(sorted(string))
            groups[check_str].append(string)
        return list(groups.values())


