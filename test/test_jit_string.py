from __future__ import absolute_import, division, print_function, unicode_literals
from test_jit import JitTestCase

class TestScript(JitTestCase):
    def test_str_ops(self):
        def test_str_is(s):
            # type: (str) -> Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]
            return s.isupper(), s.islower(), s.isdigit(), s.isspace(), \
                s.isalnum(), s.isalpha(), s.isdecimal(), s.isnumeric(), \
                s.isidentifier(), s.istitle(), s.isprintable()

        def test_str_to(s):
            # type: (str) -> Tuple[str, str, str, str, str]
            return s.upper(), s.lower(), s.capitalize(), s.title(), s.swapcase()

        def test_str_strip(s):
            # type: (str) -> Tuple[str, str, str]
            return (
              s.lstrip(),
              s.rstrip(),
              s.strip(),
            )

        def test_str_strip_char_set(s, char_set):
            # type: (str, str) -> Tuple[str, str, str]
            return (
              s.lstrip(char_set),
              s.rstrip(char_set),
              s.strip(char_set),
            )

        inputs = ["", "12a", "!B", "12", "a", "B", "aB", "$12", "B12", "AB ",
                  "  \t", "  \n", "\na", "abc", "123.3", "s a", "b12a ",
                  "more strings with spaces", "Titular Strings", "\x0acan'tprintthis",
                  "spaces at the end ", " begin"]

        def test_str_center(i, s):
            # type: (int, str) -> str
            return s.center(i)

        def test_str_center_fc(i, s):
            # type: (int, str) -> str
            return s.center(i, '*')

        def test_str_center_error(s):
            # type: (str) -> str
            return s.center(10, '**')

        def test_ljust(s, i):
          # type: (str, int) -> str
          return s.ljust(i)

        def test_ljust_fc(s, i, fc):
          # type: (str, int, str) -> str
          return s.ljust(i, fc)

        def test_ljust_fc_err(s):
          # type: (str) -> str
          return s.ljust(10, '**')

        def test_rjust(s, i):
          # type: (str, int) -> str
          return s.rjust(i)

        def test_rjust_fc(s, i, fc):
          # type: (str, int, str) -> str
          return s.rjust(i, fc)

        def test_rjust_fc_err(s):
          # type: (str) -> str
          return s.rjust(10, '**')

        def test_zfill(s, i):
          # type: (str, int) -> str
          return s.zfill(i)

        for input in inputs:
            self.checkScript(test_str_is, (input,))
            self.checkScript(test_str_to, (input,))
            self.checkScript(test_str_strip, (input,))
            for char_set in ["abc", "123", " ", "\t"]:
                self.checkScript(test_str_strip_char_set, (input, char_set))
            for i in range(7):
                self.checkScript(test_str_center, (i, input,))
                self.checkScript(test_str_center_fc, (i, input,))
                self.checkScript(test_ljust, (input, i))
                self.checkScript(test_ljust_fc, (input, i, '*'))
                self.checkScript(test_rjust, (input, i))
                self.checkScript(test_rjust_fc, (input, i, '*'))
                self.checkScript(test_zfill, (input, i))

        with self.assertRaises(Exception):
            test_str_center_error("error")
            test_ljust("error")

        def test_count():
            # type: () -> Tuple[int, int, int, int, int, int, int, int, int, int, int, int]
            return (
              "hello".count("h"),
              "hello".count("h", 0, 1),
              "hello".count("h", -3),
              "hello".count("h", -10, 1),
              "hello".count("h", 0, -10),
              "hello".count("h", 0, 10),
              "hello".count("ell"),
              "hello".count("ell", 0, 1),
              "hello".count("ell", -3),
              "hello".count("ell", -10, 1),
              "hello".count("ell", 0, -10),
              "hello".count("ell", 0, 10)
            )
        self.checkScript(test_count, ())
        def test_endswith():
            # type: () -> Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]
            return (
              "hello".endswith("lo"),
              "hello".endswith("lo", 0),
              "hello".endswith("lo", -2),
              "hello".endswith("lo", -8),
              "hello".endswith("lo", 0, -5),
              "hello".endswith("lo", -2, 3),
              "hello".endswith("lo", -8, 4),
              "hello".endswith("l"),
              "hello".endswith("l", 0),
              "hello".endswith("l", -2),
              "hello".endswith("l", -8),
              "hello".endswith("l", 0, -5),
              "hello".endswith("l", -2, 3),
              "hello".endswith("l", -8, 4)
            )
        self.checkScript(test_endswith, ())
        def test_startswith():
            # type: () -> Tuple[bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool]
            return (
              "hello".startswith("lo"),
              "hello".startswith("lo", 0),
              "hello".startswith("lo", -2),
              "hello".startswith("lo", -8),
              "hello".startswith("lo", 0, -5),
              "hello".startswith("lo", -2, 3),
              "hello".startswith("lo", -8, 4),
              "hello".startswith("l"),
              "hello".startswith("l", 0),
              "hello".startswith("l", -2),
              "hello".startswith("l", -8),
              "hello".startswith("l", 0, -5),
              "hello".startswith("l", -2, 3),
              "hello".startswith("l", -8, 4)
            )
        self.checkScript(test_startswith, ())
        def test_expandtabs():
            # type: () -> Tuple[str, str, str, str, str, str]
            return (
              'xyz\t82345\tabc'.expandtabs(),
              'xyz\t32345\tabc'.expandtabs(3),
              'xyz\t52345\tabc'.expandtabs(5),
              'xyz\t62345\tabc'.expandtabs(6),
              'xyz\t72345\tabc'.expandtabs(7),
              'xyz\t62345\tabc'.expandtabs(-5),
            )
        self.checkScript(test_expandtabs, ())

        def test_rfind():
            # type: () -> Tuple[int, int, int, int, int, int, int, int, int]
            return (
              "hello123abc".rfind("llo"),
              "hello123abc".rfind("12"),
              "hello123abc".rfind("ab"),
              "hello123abc".rfind("ll", -1),
              "hello123abc".rfind("12", 4),
              "hello123abc".rfind("ab", -7),
              "hello123abc".rfind("ll", -1, 8),
              "hello123abc".rfind("12", 4, -4),
              "hello123abc".rfind("ab", -7, -20),
            )
        self.checkScript(test_rfind, ())

        def test_find():
            # type: () -> Tuple[int, int, int, int, int, int, int, int, int]
            return (
              "hello123abc".find("llo"),
              "hello123abc".find("12"),
              "hello123abc".find("ab"),
              "hello123abc".find("ll", -1),
              "hello123abc".find("12", 4),
              "hello123abc".find("ab", -7),
              "hello123abc".find("ll", -1, 8),
              "hello123abc".find("12", 4, -4),
              "hello123abc".find("ab", -7, -20),
            )
        self.checkScript(test_find, ())

        def test_index():
            # type: () -> Tuple[int, int, int, int, int, int]
            return (
              "hello123abc".index("llo"),
              "hello123abc".index("12"),
              "hello123abc".index("ab"),
              "hello123abc".index("12", 4),
              "hello123abc".index("ab", -7),
              "hello123abc".index("12", 4, -4),
            )
        self.checkScript(test_index, ())

        def test_rindex():
            # type: () -> Tuple[int, int, int, int, int, int]
            return (
              "hello123abc".rindex("llo"),
              "hello123abc".rindex("12"),
              "hello123abc".rindex("ab"),
              "hello123abc".rindex("12", 4),
              "hello123abc".rindex("ab", -7),
              "hello123abc".rindex("12", 4, -4),
            )
        self.checkScript(test_rindex, ())

        def test_replace():
            # type: () -> Tuple[str, str, str, str, str, str, str]
            return (
              "hello123abc".replace("llo", "sdf"),
              "ff".replace("f", "ff"),
              "abc123".replace("a", "testing"),
              "aaaaaa".replace("a", "testing", 3),
              "bbb".replace("a", "testing", 3),
              "ccc".replace("c", "ccc", 3),
              "cc".replace("c", "ccc", -3),
            )
        self.checkScript(test_replace, ())

        def test_partition():
            # type: () -> Tuple[Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str]]
            return (
              "hello123abc".partition("llo"),
              "ff".partition("f"),
              "abc123".partition("a"),
              "aaaaaa".partition("testing"),
              "bbb".partition("a"),
              "ccc".partition("ccc"),
              "cc".partition("ccc"),
            )
        self.checkScript(test_partition, ())

        def test_rpartition():
            # type: () -> Tuple[Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str], Tuple[str,str,str]]
            return (
              "hello123abc".rpartition("llo"),
              "ff".rpartition("f"),
              "abc123".rpartition("a"),
              "aaaaaa".rpartition("testing"),
              "bbb".rpartition("a"),
              "ccc".rpartition("ccc"),
              "cc".rpartition("ccc"),
            )
        self.checkScript(test_rpartition, ())

        def test_split():
            # type: () -> Tuple[List[str], List[str], List[str], List[str], List[str], List[str], List[str], List[str], List[str]]
            return (
              "a a a a a".split(),
              " a a a a a ".split(" "),
              "a a a a a ".split(" ", 10),
              "a a a a a ".split(" ", -1),
              "a a a a a ".split(" ", 3),
              " a a a a a ".split("*"),
              " a*a a*a a".split("*"),
              " a*a a*a a ".split("*", -1),
              " a*a a*a a ".split("a*", 10),
            )
        self.checkScript(test_split, ())

        def test_rsplit():
            # type: () -> Tuple[List[str], List[str], List[str], List[str], List[str], List[str], List[str], List[str], List[str]]
            return (
              "a a a a a".rsplit(),
              " a a a a a ".rsplit(" "),
              "a a a a a ".rsplit(" ", 10),
              "a a a a a ".rsplit(" ", -1),
              "a a a a a ".rsplit(" ", 3),
              " a a a a a ".rsplit("*"),
              " a*a a*a a ".rsplit("*"),
              " a*a a*a a ".rsplit("*", -1),
              " a*a a*a a".rsplit("a*", 10),
            )
        self.checkScript(test_rsplit, ())

        def test_splitlines():
            # type: () -> Tuple[ List[str], List[str], List[str], List[str], List[str], List[str] ]
            return (
              "hello\ntest".splitlines(),
              "hello\n\ntest\n".splitlines(),
              "hello\ntest\n\n".splitlines(),
              "hello\vtest".splitlines(),
              "hello\v\f\ntest".splitlines(),
              "hello\ftest".splitlines(),
            )
        self.checkScript(test_splitlines, ())

        def test_str_cmp(a, b):
            # type: (str, str) -> Tuple[bool, bool, bool, bool, bool, bool]
            return a != b, a == b, a < b, a > b, a <= b, a >= b

        for i in range(len(inputs) - 1):
            self.checkScript(test_str_cmp, (inputs[i], inputs[i + 1]))


