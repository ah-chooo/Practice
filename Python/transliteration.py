from states import SymbolType


def classifier(symbol):
    if ord('a') <= ord(symbol) <= ord('f'):
        return symbol, SymbolType.SYMBOL_NUMBER_LETTER

    if ord('A') <= ord(symbol) <= ord('F'):
        return symbol, SymbolType.SYMBOL_NUMBER_LETTER

    if ord('g') <= ord(symbol) <= ord('z'):
        return symbol, SymbolType.SYMBOL_TRUE_LETTER

    if ord('G') <= ord(symbol) <= ord('Z'):
        return symbol, SymbolType.SYMBOL_TRUE_LETTER

    if ord('0') <= ord(symbol) <= ord('9'):
        return symbol, SymbolType.SYMBOL_NUMBER

    if symbol == "=":
        return symbol, SymbolType.SYMBOL_EQUALS

    if symbol == " ":
        return symbol, SymbolType.SYMBOL_SPACE

    if symbol == "-" or symbol == "+":
        return symbol, SymbolType.SYMBOL_SIGN

    if symbol == "$":
        return symbol, SymbolType.SYMBOL_DOLLAR

    if symbol == ";":
        return symbol, SymbolType.SYMBOL_SEMICOLON
    else:
        raise IOError('Error. неопознанный символ "' + symbol + '"')


def transliteration(str):
    if len(str) > 80:
        raise IOError('Error. Строка превышает 80 символов')
    answer = []

    for symbol in str:
        answer.append(classifier(symbol))

    return answer
