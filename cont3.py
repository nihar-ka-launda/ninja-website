class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        char = []
        count = [0]*len(word)
        
        for ch in word:
            if not(char and char[-1] == ch):
                char.append(ch)
            count[len(char)-1] += 1
        
        v = ("a", "e", "i", "o", "u")
        vi = 0
        
        
        long = 0
        current = 0
        for i, ch in enumerate(char):
            if vi == len(v):
                # print(i)
                long = max(long, current)
                vi = 0
            if ch != v[vi]:
                vi = 0
                current = 0
            current += count[i]
            vi += 1
            
        if vi == len(v):
            long = max(long, current)
        return long

s = Solution()
s.longestBeautifulSubstring("auoeioueiaaioeuieuoaieuaoeuoaiaoueioiaeuiuaeouaoie")