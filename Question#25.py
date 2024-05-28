# In English, the present participle is formed by adding the suffix ing to the infinite form: go > going. A simple
# set of heuristic rules can be given as follows:
# 1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 2. If the verb ends in ie, change ie to y and add ing
# 3. For words consisting of consonant vowel consonant, double the final letter before adding ing
# 4. By default, just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
# returns its present participle form. Test your function with words such as lie, see, move and hug. However,
# you must not expect such simple rules to work for all cases.

def make_3sg_form(verb):
    list_verb = list(verb)
    if verb.endswith("ie"):
        list_verb[-2:] = "ying"
        return "".join(list_verb)
    elif verb.endswith("e"):
        list_verb[-1] = "ing"
        return "".join(list_verb)
    elif verb.endswith(("a", "e", "i", "o", "u")):
        list_verb[-1] = list_verb[-1]+list_verb[-1]+"ying"
        return "".join(list_verb)
    else:
        list_verb.append("ing")
        return "".join(list_verb)


print(make_3sg_form("lie"))
print(make_3sg_form("see"))
print(make_3sg_form("move"))
print(make_3sg_form("hug"))
