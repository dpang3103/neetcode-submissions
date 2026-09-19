class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            check_str = "".join(sorted(string))
            if check_str in groups:
                groups[check_str].append(string)
            else:
                groups[check_str] = [string]
        return list(groups.values())


