s1='listen'

s2='silenu'

def anagram(s1,s2):
    s1=set(s1)
    s2=set(s2)
    if s1==s2:
        return True
    else:
        return False
print(anagram(s1,s2))
