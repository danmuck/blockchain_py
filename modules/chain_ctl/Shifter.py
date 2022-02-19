dict_ = {
    'a': '9',
    'b': '8',
    'c': '7',
    'd': '6',
    'e': '5',
    'f': '4',
    'g': '3',
    'h': '2',
    'i': '1',
    'j': '0',
    'k': 'a',
    'l': 'b',
    'm': 'c',
    'n': 'd',
    'o': 'e',
    'p': 'f',
    'q': 'g',
    'r': 'h',
    's': 'i',
    't': 'j',
    'u': 'k',
    'v': 'l',
    'w': 'm',
    'x': 'n',
    'y': 'o',
    'z': 'p',
    '0': 'q',
    '1': 'r',
    '2': 's',
    '3': 't',
    '4': 'u',
    '5': 'v',
    '6': 'w',
    '7': 'x',
    '8': 'y',
    '9': 'z',
}

def shifter_(str_:str) -> str:
    new_hash = 'dp'
    if len(str_) != 66:
        pass
    else: 
        for char in str_[2:]:
            char = dict_.get(str(char))
            new_hash = (new_hash + str(char))
    if len(new_hash) != 66:
        pass
    else:
        return new_hash
