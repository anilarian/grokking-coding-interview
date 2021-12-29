"""Conflicting Appointments (medium)


Problem Statement

Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.


Solution

The problem follows the Merge Intervals pattern. We can sort all the intervals by start time and then check if any two intervals overlap. A person will not be able to attend all appointments if any two appointments overlap.

"""


class Appointment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.interval = [self.start, self.end]


def check_conflicting_appointments(appointments: [Appointment]):
    appointments.sort(key=lambda x: x.start)
    end = appointments[0].end
    overlapping = False

    for i in range(1, len(appointments)):
        current_appt = appointments[i]
        if current_appt.start < end:
            overlapping = True
            break
        end = current_appt.end
    return overlapping


def main():
    print("schedule has conflicts: {}".format(check_conflicting_appointments([Appointment(1, 4), Appointment(2, 5), Appointment(7, 9)])))
    print("schedule has conflicts: {}".format(check_conflicting_appointments([Appointment(1, 4), Appointment(4, 5), Appointment(7, 9)])))

main()
