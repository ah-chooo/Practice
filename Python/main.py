import in_out
import transliteration
import lexical
import syntactic

lines = in_out.read()

for line in lines:

    try:
        transliteration_result = transliteration.transliteration(line)
        # print(transliteration_result)
        lexical_result = lexical.lexical(transliteration_result)
        # print(lexical_result)
        syntactic.syntactic(lexical_result)
        in_out.write("ACCEPT")
    except Exception as e:
        in_out.write("REJECT")
        print(e)
