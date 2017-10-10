import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)


# conversion dict
d = {'A': '.-',
     'B': '-...',
     'C': '-.-.',
     'D': '-..',
     'E': '.',
     'F': '..-.',
     'G': '--.',
     'H': '....',
     'I': '..',
     'J': '.---',
     'K': '-.-',
     'L': '.-..',
     'M': '--',
     'N': '-.',
     'O': '---',
     'P': '.--.',
     'Q': '--.-',
     'R': '.-.',
     'S': '...',
     'T': '-',
     'U': '..-',
     'V': '...-',
     'W': '.--',
     'X': '-..-',
     'Y': '-.--',
     'Z': '--..'
     }


def replace(s):
    '''replace letters with morse code'''
    res = ''
    for c in s:
        res += d[c]
    return res


@lru_cache(maxsize=None)
def solve(start, _str):
    '''Recursively solve the puzzle.'''
    
    if start == len(_str):
        return 1

    res = 0
    for word in words:
        if _str[start:start + len(word)] == word:
            res += solve(start + len(word), _str)
    return res


# get input
L = input()
N = int(input())
words = [input() for _ in range(N)]

# convert to morse code and remove all which are not possible
words = [replace(x) for x in words]
words = [x for x in words if x in L]

print(solve(0, L))
