"""Problem Challenge 1: Minimum Meeting Rooms (hard)


Problem Statement

Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example 1:

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
occur in any of the two rooms later.
Example 2:

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
Example 3:

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
hold all the meetings.

Example 4:

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

Here is a visual representation of Example 4:"""
import heapq


class Appointment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.interval = [self.start, self.end]


def minimum_meeting_rooms(appointments: [Appointment] = None):
    if not appointments:
        return 0

    appointments.sort(key=lambda x: x.start)
    min_rooms = 0
    min_heap = []

    # add first meeting end time to heap
    heapq.heappush(min_heap, appointments[0].end)

    # iterate through the rest of appointments and check if there is a meeting with
    # start time < earliest ending meeting;if start time < earliest end time add that meeting to the heap
    # else pop the existing meeting and compare next

    for appointment in appointments[1:]:
        if appointment.start >= min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, appointment.end)
        min_rooms = max(min_rooms, len(min_heap))
    return min_rooms


def main():
    print("minimum rooms required: {}".format(
        minimum_meeting_rooms([Appointment(1, 4), Appointment(2, 5), Appointment(7, 9)])))
    print("minimum rooms required: {}".format(
        minimum_meeting_rooms([Appointment(1, 4), Appointment(3, 5), Appointment(3, 9)])))
    print("minimum rooms required: {}".format(
        minimum_meeting_rooms()))


main()
