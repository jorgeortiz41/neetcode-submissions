class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty list"
        result = '✅'.join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        if s == "empty list":
            return []
        result = s.split('✅') #if len(s) > 0 else [""]
        return result