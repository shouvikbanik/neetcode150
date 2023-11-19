from unittest import TestCase

from group_anagrams import group_anagrams, create_tuples_from_string


class Test(TestCase):
    def test_group_anagrams(self):
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
                         group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    def test_create_list_of_tuples(self):
        check_val = [0] * 26
        check_val[0] = 2
        check_val[1] = 1
        self.assertEqual(tuple(check_val), create_tuples_from_string("aba"))
