def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    if len(needle)==0:
        return 0
    return -1


print(strStr("hello","ll"))