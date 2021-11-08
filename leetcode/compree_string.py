
def compress(s):

    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s + '1'
    cnt = 1
    i =1
    res =''
    while i < len(s):
        if s[i] == s[i-1]:
            cnt +=1
        else:
            res += s[i-1] + str(cnt)
            cnt = 1
        i += 1
    res += s[i-1] + str(cnt)
    return res

print(compress('AAAABBBBCCCCCDDEEEE' ))
