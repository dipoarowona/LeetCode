def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) ==0:
        return ''
    ans = []
    count = 0
    
    for letter in strs[0]:
        cont = True
        for i in range(1,len(strs)):
            if count == len(strs[i]) or letter != strs[i][count]:
                cont = False
                break
        if cont:
            ans.append(letter)
        else:
            break
        count+=1
    
    
    return "".join(ans).strip()


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))