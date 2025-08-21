class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        S2T = {}
        T2S = {}

        for sc, tc in zip(s, t):
            if sc in S2T and S2T[sc] != tc:
                return False
            if tc in T2S and T2S[tc] != sc:
                return False
            S2T[sc] = tc
            T2S[tc] = sc

        return True
