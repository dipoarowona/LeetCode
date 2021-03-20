class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = {}
        j = 0
        l =0
        for i in pattern:
            temp=""
            while j<len(s) and (s[j]!= " " or len(s)-1==j):
                temp = temp + s[j]
                j+=1            
            if j<len(s) and s[j]==" ":
                l+=1
                j+=1
            if i in words.keys():
                if words[i] != temp:
                    return False
            else:
                if temp in words.values():
                    return False
                else:
                    words[i] = temp
        print(l+1,len(pattern))
              
        return l+1==len(pattern)