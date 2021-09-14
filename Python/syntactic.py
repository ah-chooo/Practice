from states import StatesSyntactic
from states import StatesLexical


def classifier(current_state, lexeme):
    # print(lexeme)
    if current_state == StatesSyntactic.STATE_START:
        if lexeme[1] == StatesLexical.STATE_KEY_CONST:
            return StatesSyntactic.STATE_KEY_CONST

    if current_state == StatesSyntactic.STATE_KEY_CONST:
        if lexeme[1] == StatesLexical.STATE_ID:
            return StatesSyntactic.STATE_NAME

    if current_state == StatesSyntactic.STATE_NAME:
        if lexeme[1] == StatesLexical.STATE_EQUALS:
            return StatesSyntactic.STATE_EQUALS

    if current_state == StatesSyntactic.STATE_EQUALS:
        if lexeme[1] == StatesLexical.STATE_SIGN:
            return StatesSyntactic.STATE_SIGN

        if lexeme[1] == StatesLexical.STATE_INTEGER:
            return StatesSyntactic.STATE_INTEGER

        if lexeme[1] == StatesLexical.STATE_DOLLAR:
            return StatesSyntactic.STATE_DOLLAR

    if current_state == StatesSyntactic.STATE_SIGN:
        if lexeme[1] == StatesLexical.STATE_INTEGER:
            return StatesSyntactic.STATE_INTEGER

    if current_state == StatesSyntactic.STATE_INTEGER:
        if lexeme[1] == StatesLexical.STATE_SEMICOLON:
            return StatesSyntactic.STATE_SEMICOLON

    if current_state == StatesSyntactic.STATE_DOLLAR:
        if lexeme[1] == StatesLexical.STATE_HEXADECIMAL_WORD:
            return StatesSyntactic.STATE_HEXADECIMAL

    if current_state == StatesSyntactic.STATE_HEXADECIMAL:
        if lexeme[1] == StatesLexical.STATE_SEMICOLON:
            return StatesSyntactic.STATE_SEMICOLON

    raise IOError('Syntactic error. Неожиданая лексема "' + lexeme[0] + '"')


def syntactic(lexemes):
    current_state = StatesSyntactic.STATE_START

    for lexeme in lexemes:
        current_state = classifier(current_state, lexeme)

    if not current_state == StatesSyntactic.STATE_SEMICOLON:
        raise IOError('Syntactic error. Строка не завершилась символом ";"')
