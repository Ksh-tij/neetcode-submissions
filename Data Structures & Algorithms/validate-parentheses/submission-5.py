class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hmap = { ")":"(","]":"[","}":"{"}
        for c in s:
            if c in hmap:
                if stk and stk[-1] == hmap[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return not stk
        