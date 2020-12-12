def ValidAnagram1(s, t):
    return sorted(s) == sorted(t)


def ValidAnagram2(s, t):
    ls = list(s)
    lt = list(t)
    lt.sort()
    ls.sort()
    return ls == lt


print(ValidAnagram1("ye", "esy"))
print(ValidAnagram2("eys", "yes"))
