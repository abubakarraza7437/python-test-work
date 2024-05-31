# In English, the present participle is formed by adding the suffix ing to the infinite form: go > going. A simple
# set of heuristic rules can be given as follows:
# 1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 2. If the verb ends in ie, change ie to y and add ing
# 3. For words consisting of consonant vowel consonant, double the final letter before adding ing
# 4. By default, just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
# returns its present participle form. Test your function with words such as lie, see, move and hug. However,
# you must not expect such simple rules to work for all cases.

import unittest


def make_3sg_form(verb):
    if verb.endswith("y") and not verb.endswith("ay") and not verb.endswith("ey") and not verb.endswith(
            "iy") and not verb.endswith("oy") and not verb.endswith("uy"):
        return verb[:-1] + "ies"
    elif verb.endswith("o") or verb.endswith("ch") or verb.endswith("s") or verb.endswith("sh") or verb.endswith(
            "x") or verb.endswith("z"):
        return verb + "es"
    else:
        return verb + "s"


print(make_3sg_form("lie"))
print(make_3sg_form("see"))
print(make_3sg_form("move"))
print(make_3sg_form("hug"))


class TestCal(unittest.TestCase):

    def test_y_ending(self):
        self.assertEqual(make_3sg_form("try"), "tries")

    def test_ends_with_ch(self):
        self.assertEqual(make_3sg_form("watch"), "watches")

    def test_ends_with_s(self):
        self.assertEqual(make_3sg_form("kiss"), "kisses")

    def test_ends_with_o(self):
        self.assertEqual(make_3sg_form("go"), "goes")

    def test_ends_with_sh(self):
        self.assertEqual(make_3sg_form("brush"), "brushes")

    def test_ends_with_x(self):
        self.assertEqual(make_3sg_form("fix"), "fixes")

    def test_general_case(self):
        self.assertEqual(make_3sg_form("run"), "runs")


if __name__ == "__main__":
    unittest.main()