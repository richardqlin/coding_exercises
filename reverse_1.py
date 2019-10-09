'''

Given a string of words, reverse all the words

start ="This is the best"
finish ="best the is This"

'''

def reverse(s):

    return ' '.join(reversed(s.split()))

start ="This is the best"

print(reverse(start))

def reverse1(s):
    length = len(s)
    spaces = [' ']
    words = []
    i = 0

    while i<length:
        if s[i] not in spaces:
            word_start = i

            while i <length and s[i] not in spaces:
                i += 1

            words .append(s[word_start:i])
        i += 1
    return ''.join(reversed(s))

print(reverse1(start))

def rev(s):
    return s.split()[::-1]

print(rev('Hello, I and Grant'))
