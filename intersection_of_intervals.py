"""Intervals Intersection (medium)


Problem Statement

Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
Solution

This problem follows the Merge Intervals pattern. As we have discussed under Insert Interval,
there are five overlapping possibilities between two intervals ‘a’ and ‘b’. A close observation will
tell us that whenever the two intervals overlap, one of the interval’s start time lies within the
other interval. This rule can help us identify if any two intervals overlap or not.


Now, if we have found that the two intervals overlap, how can we find the overlapped part?

Again from the above diagram, the overlapping interval will be equal to:

    start = max(a.start, b.start)
    end = min(a.end, b.end)
That is, the highest start time and the lowest end time will be the overlapping interval.

So our algorithm will be to iterate through both the lists together to see if any two intervals
overlap. If two intervals overlap, we will insert the overlapped part into a result list and move on
to the next interval which is finishing early.

Code"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.interval = [self.start, self.end]

    def print_interval(self):
        print(self.interval)


def intersection(intervals1: [Interval], intervals2: [Interval]):
    intersect = []
    i, j, = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        a_overlaps_b = intervals2[j].start <= intervals1[i].start <= intervals2[j].end
        b_overlaps_a = intervals1[i].start <= intervals2[j].start <= intervals1[i].end

        if a_overlaps_b or b_overlaps_a:
            start = max(intervals1[i].start, intervals2[j].start)
            end = min(intervals1[i].end, intervals2[j].end)
            intersect.append(Interval(start, end))

        if intervals1[i].end < intervals2[j].end:
            i += 1
        else:
            j += 1
    return intersect


def main():
    intersect = intersection([Interval(1, 3), Interval(5, 9), Interval(7, 12)],
                             [Interval(2, 3), Interval(5, 10)])
    for inter in intersect:
        inter.print_interval()


main()
