from states import StatesLexical


def binary_search(key_words, id):
    first = 0
    last = len(key_words) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if key_words[mid] == id:
            index = mid
        else:
            if id < key_words[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


def search(id):
    admission = binary_search((
        'and', 'array', 'begin', 'case', 'const', 'div', 'do', 'downto', 'else',
        'end', 'file', 'for', 'function', 'goto', 'if', 'in', 'label', 'mod', 'nil',
        'not', 'of', 'or', 'packed', 'procedure', 'program', 'record', 'repeat',
        'set', 'then', 'to', 'type', 'until', 'var', 'while', 'with'
    ), id.lower())

    if admission == -1:
        return StatesLexical.STATE_ID

    if admission == 4:
        return StatesLexical.STATE_KEY_CONST

    return StatesLexical.STATE_KEY_ANOTHER

# print(search('wowow'))                     # автономное тестирование блока идентификации на заданном идентификаторе
