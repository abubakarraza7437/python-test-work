# The third person singular verb form in English is distinguished by the suffix s,
# which is added to the stem of
# the infinitive form: run >
# runs. A simple set of rules can be given as follows:
# 1. If the verb ends in y, remove it and add ies
# 2. If the verb ends in o, ch, s, sh, x or z, add es
# 3. By default just add s
# Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form
# returns its third person singular form. Test your function with words like try, brush, run and fix. Note however
# that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all
# cases. Tip: Check out the string method endswith()

def make_3sg_form(verb):
    list_verb = list(verb)
    if verb.endswith("y"):
        list_verb[-1] = "ies"
        return "".join(list_verb)
    elif verb.endswith(("o",  "ch", "s", "sh", "x", "z")):
        list_verb.append("es")
        return "".join(list_verb)
    else:
        list_verb.append("s")
        return "".join(list_verb)


print(make_3sg_form("try"))
print(make_3sg_form("brush"))
print(make_3sg_form("run"))
print(make_3sg_form("fix"))


