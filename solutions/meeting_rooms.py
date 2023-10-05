def can_attend_meetings(intervals):
    intervals.sort(key=lambda i: i.start)
    for index in range(1, len(intervals)):
        if intervals[index - 1].end > intervals[index].start:
            return False
    return True
