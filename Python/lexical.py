from states import SymbolType
from states import StatesLexical
import identification


def classifier(lexeme, current_state):
    # print(lexeme)
    # print(current_state)
    if current_state == StatesLexical.STATE_START:
        if lexeme[1] == SymbolType.SYMBOL_TRUE_LETTER:
            return StatesLexical.STATE_ID

        if lexeme[1] == SymbolType.SYMBOL_NUMBER_LETTER:
            return StatesLexical.STATE_ID

        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_START

    if current_state == StatesLexical.STATE_ID:
        if lexeme[1] == SymbolType.SYMBOL_TRUE_LETTER:
            return StatesLexical.STATE_ID

        if lexeme[1] == SymbolType.SYMBOL_NUMBER_LETTER:
            return StatesLexical.STATE_ID

        if lexeme[1] == SymbolType.SYMBOL_NUMBER:
            return StatesLexical.STATE_ID

        if lexeme[1] == SymbolType.SYMBOL_EQUALS:
            return StatesLexical.STATE_EQUALS

        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_SPACE_1

    if current_state == StatesLexical.STATE_SPACE_1:
        if lexeme[1] == SymbolType.SYMBOL_TRUE_LETTER:
            return StatesLexical.STATE_ID

        if lexeme[1] == SymbolType.SYMBOL_NUMBER_LETTER:
            return StatesLexical.STATE_ID

        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_SPACE_1

        if lexeme[1] == SymbolType.SYMBOL_EQUALS:
            return StatesLexical.STATE_EQUALS

    if current_state == StatesLexical.STATE_EQUALS:
        if lexeme[1] == SymbolType.SYMBOL_NUMBER:
            return StatesLexical.STATE_INTEGER

        if lexeme[1] == SymbolType.SYMBOL_SIGN:
            return StatesLexical.STATE_SIGN

        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_EQUALS

        if lexeme[1] == SymbolType.SYMBOL_DOLLAR:
            return StatesLexical.STATE_DOLLAR

    if current_state == StatesLexical.STATE_SIGN:
        if lexeme[1] == SymbolType.SYMBOL_NUMBER:
            return StatesLexical.STATE_INTEGER

        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_SIGN

    if current_state == StatesLexical.STATE_INTEGER:
        if lexeme[1] == SymbolType.SYMBOL_NUMBER:
            return StatesLexical.STATE_INTEGER

        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_SPACE_5

        if lexeme[1] == SymbolType.SYMBOL_SEMICOLON:
            return StatesLexical.STATE_SEMICOLON

    if current_state == StatesLexical.STATE_SPACE_5:
        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_SPACE_5

        if lexeme[1] == SymbolType.SYMBOL_SEMICOLON:
            return StatesLexical.STATE_SEMICOLON

    if current_state == StatesLexical.STATE_DOLLAR:
        if lexeme[1] == SymbolType.SYMBOL_NUMBER_LETTER:
            return StatesLexical.STATE_HEXADECIMAL_WORD

        if lexeme[1] == SymbolType.SYMBOL_NUMBER:
            return StatesLexical.STATE_HEXADECIMAL_WORD

        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_SPACE_5

    if current_state == StatesLexical.STATE_HEXADECIMAL_WORD:
        if lexeme[1] == SymbolType.SYMBOL_NUMBER_LETTER:
            return StatesLexical.STATE_HEXADECIMAL_WORD

        if lexeme[1] == SymbolType.SYMBOL_NUMBER:
            return StatesLexical.STATE_HEXADECIMAL_WORD

        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_SPACE_5

        if lexeme[1] == SymbolType.SYMBOL_SEMICOLON:
            return StatesLexical.STATE_SEMICOLON

    if current_state == StatesLexical.STATE_SEMICOLON:
        if lexeme[1] == SymbolType.SYMBOL_SPACE:
            return StatesLexical.STATE_SEMICOLON

    raise IOError('Error. Неожиданая лексема "' + lexeme[0] + '"')


def lexical(lexeme_list):
    current_state = StatesLexical.STATE_START
    current_word = ""
    words = []

    for lexeme in lexeme_list:
        new_state = classifier(lexeme, current_state)

        if not new_state == current_state:
            if current_state == StatesLexical.STATE_ID:
                current_state = identification.search(current_word)

            if len(current_word):
                words.append((current_word, current_state))

            current_word = ""

        if not lexeme[1] == SymbolType.SYMBOL_SPACE:
            current_word += lexeme[0]

        current_state = new_state

    if len(current_word):
        words.append((current_word, current_state))

    return words
