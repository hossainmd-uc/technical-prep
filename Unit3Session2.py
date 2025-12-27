# Problem 1: Manage Performance Stage Changes

"""
At a cultural festival, multiple performances are scheduled on a single stage.
However, due to last-minute changes, some performances need to be rescheduled
or canceled. The festival organizers use a stack to manage these changes
efficiently.

You are given a list changes of strings where each string represents a change
action. The actions can be:

    "Schedule X": Schedule a performance with ID X on the stage.
    "Cancel": Cancel the most recently scheduled performance that hasn't been
    canceled yet.
    "Reschedule": Reschedule the most recently canceled performance to be the
    next on stage.

Return a list of performance IDs that remain scheduled on the stage after all
changes have been applied.
"""


def manage_stage_changes(changes):

    res = []
    c = []

    for each in changes:
        s = each.split(" ")
        if len(s) > 1:
            res.append(s[1])

        if each == "Cancel" and len(res) > 0:
            c.append(res.pop())
        if each == "Reschedule" and len(c) > 0:
            res.append(c.pop())

    return res


# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"]))
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))


# Problem 2: Queue of Performance Requests

"""
You are organizing a festival and want to manage the queue of requests to perform. 
Each request has a priority. Use a queue to process the performance requests in the 
order they arrive but ensure that requests with higher priorities are processed 
before those with lower priorities. Return the order in which performances are 
processed.
"""
import math
from collections import deque


def process_performance_requests(requests):
    dq = deque(requests)
    max_list = []

    while dq:  # n complexity since 1 item is removed each time
        max_val = (-math.inf, None)
        for _ in range(len(dq)):  # n complexity since we need to check whole
            popped = dq.popleft()
            # print('popped', popped)
            if popped[0] > max_val[0]:
                if (
                    max_val[1] != None
                ):  # if we currently have a max occupying, then reque
                    dq.append(max_val)  # since there is a new max
                max_val = popped

            else:
                dq.append(popped)  # perpetrator line (had wrong element added back)

        max_list.append(max_val)

    return [y for _, y in max_list]


# def process_performance_requests_refined(requests):
#     dq = deque()


# print(process_performance_requests([(3, "Dance"), (5, "Music"), (1, "Drama")]))
# print(
#     process_performance_requests(
#         [(2, "Poetry"), (1, "Magic Show"), (4, "Concert"), (3, "Stand-up Comedy")]
#     )
# )
# print(
#     process_performance_requests(
#         [
#             (1, "Art Exhibition"),
#             (3, "Film Screening"),
#             (2, "Workshop"),
#             (5, "Keynote Speech"),
#             (4, "Panel Discussion"),
#         ]
#     )
# )

# Problem 3: Collecting Points at Festival Booths
"""
At the festival, there are various booths where visitors can collect points. 
Each booth has a specific number of points available. Use a stack to simulate
the process of collecting points and return the total points collected after 
visiting all booths.
"""


def collect_festival_points(points):
    s = []
    for i in range(len(points)):
        s.append(points[i])

    return sum([s.pop() for _ in range(len(s))])


# print(collect_festival_points([5, 8, 3, 10]))
# print(collect_festival_points([2, 7, 4, 6]))
# print(collect_festival_points([1, 5, 9, 2, 8]))

# Problem 4: Festical Booth Navigation
"""
At the cultural festival, you are managing a treasure hunt where participants 
need to visit booths in a specific order. The order in which they should visit 
the booths is defined by a series of clues. However, some clues lead to dead ends, 
and participants must backtrack to previous booths to continue their journey.

You are given a list of clues, where each clue is either a booth number (an integer)
to visit or the word "back" indicating that the participant should backtrack to the
previous booth.

Write a function to simulate the participant's journey and return the final 
sequence of booths visited, in the order they were visited.
"""


def booth_navigation(clues):
    s = []

    for each in clues:
        if isinstance(each, str) and each == "back":
            if len(s) > 0:
                s.pop()
        else:
            s.append(each)
    return s


# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues))

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues))

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues))

"""
You are organizing a cultural festival and have two performance schedules, 
schedule1 and schedule2, each represented by a string where each character 
corresponds to a performance slot. Merge the schedules by adding performances 
in alternating order, starting with schedule1. If one schedule is longer than
the other, append the additional performances onto the end of the merged schedule.
"""


def merge_schedules(schedule1, schedule2):
    a = len(schedule1)
    b = len(schedule2)

    res = []
    m = min(a, b)

    for i in range(m):
        res.append(schedule1[i])
        res.append(schedule2[i])

    if a > b:
        res.extend(schedule1[m:a])
    elif b > a:
        res.extend(schedule2[m:b])

    return "".join(res)


# print(merge_schedules("abc", "pqr"))
# print(merge_schedules("ab", "pqrs"))
# print(merge_schedules("abcd", "pq"))

"""
At a cultural festival, you have a schedule of events where each event has 
a unique popularity score. The schedule is represented by two distinct 0-indexed
integer arrays schedule1 and schedule2, where schedule1 is a subset of schedule2.

For each event in schedule1, find its position in schedule2 and determine the 
next event in schedule2 with a higher popularity score. If there is no such event, 
then the answer for that event is -1.

Return an array ans of length schedule1.length such that ans[i] is the next greater
event's popularity score as described above.
"""


def next_greater_event(schedule1, schedule2):
    res = []
    for i in range(len(schedule1)):
        c = False
        idx = schedule2.index(schedule1[i])
        for j in range(
            idx + 1, len(schedule2)
        ):  # won't resolve in error cause 1 is subset of 2
            if schedule2[j] > schedule1[i]:
                res.append(schedule2[j])
                c = True
                break
        if not c:
            res.append(-1)

    return res


# print(next_greater_event([4, 1, 2], [1, 3, 4, 2]))
# print(next_greater_event([2, 4], [1, 2, 3, 4]))

"""
You are organizing a cultural festival and have a list of performances represented
by an integer array performances. Each performance is classified as either an even 
type (e.g., dance, music) or an odd type (e.g., drama, poetry).

Your task is to rearrange the performances so that all the even-type performances
appear at the beginning of the array, followed by all the odd-type performances.

Return any array that satisfies this condition.
"""


def sort_performances_by_type_v2(performances):  # more space-optimal

    next_empty = 0

    for i in range(len(performances)):
        if performances[i] % 2 == 0:
            temp = performances[next_empty]
            performances[next_empty] = performances[i]
            performances[i] = temp

            next_empty += 1

    return performances


def sort_performances_by_type(performances):
    res = deque()

    for each in performances:
        if each % 2 == 0:
            res.appendleft(each)
        else:
            res.append(each)

    return list(res)


# print(sort_performances_by_type_v2([3, 1, 2, 4]))
# print(sort_performances_by_type_v2([0]))

# Problem 1: Final Costs After a Supply Discount

"""
You are managing the budget for a global expedition, where the cost of supplies 
is represented by an integer array costs, where costs[i] is the cost of the ith
supply item.

There is a special discount available during the expedition. If you purchase the
ith item, you will receive a discount equivalent to costs[j], where j is the minimum
index such that j > i and costs[j] <= costs[i]. If no such j exists, you will not 
receive any discount.

Return an integer array final_costs where final_costs[i] is the final cost you 
will pay for the ith supply item, considering the special discount.

"""


def final_supply_costs(costs):
    final_cost = []
    
    for i in range(len(costs)):
        found = False
        # print(f"looking for idx where val <{costs[i]}")
        for j in range (i+1, len(costs)):
            a = costs[i]
            b = costs[j]
            if costs[j] <= costs[i]:
                # print(costs[j], 'is <=', costs[i])
                # print(j)
                final_cost.append(a-b)
                found = True
                break
        if not found: # min item in list case
            final_cost.append(costs[i])
    
    return final_cost
            
def final_supply_costs_stack(costs): # improvement of time to O(n)
    
    final_cost = []
    s = []
    
    current = 0
    while current < len(costs): #while all items have not been processed
        
        while len(s) > 0: #while there still items in the stack
        
            if len(s) > 1 and s[-1] > costs[current]: #if next > last on stack
                final_cost.append(s.pop()-costs[current])
                current+=1
                 
        s.append(costs[current]) #add first item and subsequent items
        
        final_cost.extend(list(s))
        
        
        
    
    return final_cost

print(final_supply_costs_stack([8, 4, 6, 2, 3]))
# print(final_supply_costs([1, 2, 3, 4, 5]))
# print(final_supply_costs([10, 1, 1, 6]))


