def is_anagram(s:str,t:str)->bool:

    dict_s={}
    dict_t={}
    if len(s)!=len(t):
        return False
    else:
        for c in s:
            if c in dict_s:
               dict_s[c]+=1
            else:
               dict_s[c]=1
        for c in t:
            if c in dict_t:
               dict_t[c]+=1
            else:
                dict_t[c]=1
        return dict_s==dict_t

assert is_anagram("anagram", "nagaram") is True
assert is_anagram("rat", "car") is False
assert is_anagram("aab", "abb") is False
assert is_anagram("", "") is True
assert is_anagram("a", "aa") is False

print("全部测试通过！")

# scores = {"python": 4}
#
# scores["java"] = scores.get("java", 0) + 3
# print(scores)
# bb={'python': 4, 'java': 3}
# print(bb==scores)