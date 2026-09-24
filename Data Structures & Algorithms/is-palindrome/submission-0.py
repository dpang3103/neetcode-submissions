import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleansed_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower().replace(" ",""))
        print(cleansed_string)
        for letter in range(len(cleansed_string)):
            if cleansed_string[letter] == cleansed_string[-letter-1]:
                continue
            else:
                return False
        return True

        