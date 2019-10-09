'''Given a string, are all characters unqiue?
should give a True or False return

Uses python built in structures
'''

def unique(string):
    string = string.replace(' ','')
    return len(set(string)) == len(string)

print(unique('a b cdef'))

def uniq(s):
    s = s.replace(' ','')
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True


print(uniq('i jkl w cdef'))
