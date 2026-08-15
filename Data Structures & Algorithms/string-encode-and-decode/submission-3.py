class Solution:

    def encode(self, strs: List[str]) -> str:
        encStr = ""
        for s in strs:
            l = len(s)
            encStr += (str(l)+"#"+s)
        return encStr

    def decode(self, s: str) -> List[str]:
        res = []
        print(s)
        p = 0
        while p < len(s):
            j = p
            while s[j] != "#":
                j += 1
            length = int(s[p:j])
            res.append(s[j + 1: j + 1 + length])
            p = j + 1 + length

        return res
