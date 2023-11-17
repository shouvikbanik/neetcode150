from unittest import TestCase

from meeting_rooms import can_attend_meetings


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Test(TestCase):
    def test_can_attend_meetings_positive(self):
        self.assertEqual(True, can_attend_meetings([Interval(2, 3), Interval(3, 4), Interval(1, 2), Interval(6, 7)]))

    def test_can_attend_meetings_negative(self):
        self.assertEqual(False, can_attend_meetings([Interval(2, 3), Interval(3, 4), Interval(1, 2), Interval(2, 4)]))
