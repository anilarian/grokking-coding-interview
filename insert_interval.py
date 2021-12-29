"""Insert Interval (medium)


Problem Statement

Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.interval = [self.start, self.end]

    def print_interval(self):
        print(self.interval)


def merge_intervals(intervals: [Interval]):
    merged_interval = []
    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        if current_interval.start < end:
            end = max(current_interval.end, end)
        else:
            merged_interval.append(Interval(start, end))
            start = current_interval.start
            end = current_interval.end
    merged_interval.append(Interval(start, end))
    return merged_interval


def insert_interval_merge(intervals: [Interval], new_interval: Interval):
    intervals.append(new_interval)
    merged = merge_intervals(intervals)
    for interval in merged:
        interval.print_interval()


# def main():
#     insert_interval_merge([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6))
#     # print("Intervals after inserting the new interval: " +
#     #       str(insert_interval_merge([[1, 3], [5, 7], [8, 12]], [4, 10])))
#     # print("Intervals after inserting the new interval: " +
#     #       str(insert_interval_merge([[2, 3], [5, 7]], [1, 4])))
#
#
# main()


def insert_interval(intervals: [Interval], new_interval: Interval):
    intervals.sort(key=lambda x: x.start)
    merged = []
    i, start, end = 0, 0, 1

    # add intervals that are before the new interval
    while i < len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i += 1

    # merge the new interval
    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)
        merged.append(new_interval)
        i += 1

    # add remaining intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    for interval in merged:
        interval.print_interval()


def main():
    insert_interval([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6))


main()
