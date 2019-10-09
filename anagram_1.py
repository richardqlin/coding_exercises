def anagram(s1,s2):
    return sorted(s1)==sorted(s2)


print(anagram('god','dog'))


s3='god'

s=sorted(s3)

print(s)



def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

s1 = 'god'
s2 = 'dog'

print(anagram2(s1,s2))
    
