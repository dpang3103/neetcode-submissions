class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = {}
        for index, string in enumerate(strs):
            check_str = "".join(sorted(string))
            if check_str in sorted_strings:
                sorted_strings[check_str].append(index)
            else:
                sorted_strings[check_str] = [index]
        grouped_anagrams = []
        for sorted_string in sorted_strings:
            group = []
            for index in sorted_strings[sorted_string]:
                group.append(strs[index])
            grouped_anagrams.append(group)
        return grouped_anagrams

