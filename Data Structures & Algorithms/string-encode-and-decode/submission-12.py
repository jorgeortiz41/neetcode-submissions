class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty list"
        result = '✅'.join(strs)
        print("encoded: ",result)
        return result

    def decode(self, s: str) -> List[str]:
        if s == "empty list":
            return []
        print("decode input and length: ", s, len(s))
        result = s.split('✅') #if len(s) > 0 else [""]
        print("decoded: ",result)
        return result