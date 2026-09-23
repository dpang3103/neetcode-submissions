class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "√"
        joined_string = "£".join(strs)
        # print(joined_string)
        return joined_string

    def decode(self, s: str) -> List[str]:
        if s == "√":
            return []
        if s == "":
            return [""]
        decoded_string = s.split("£")
        return decoded_string
