from linked_list import LinkedList
import datetime


def get_schedule(seed):
    # create linked list
    num_groups = 6
    group_chain = LinkedList(1)
    for group in range(2, num_groups + 1):
        group_chain.append(group)
    group_chain.tail.next = group_chain.head

    # produce schedule
    node = group_chain.search(seed)
    schedule = []
    for day in range(0,6):
        schedule.append(node.value)
        node = node.next
    return schedule


def lords_date(send_date):
    lords_day = send_date
    if lords_day.weekday() == 6:
        lords_day += datetime.timedelta(1)
    while lords_day.weekday() != 6:
        lords_day += datetime.timedelta(1)
    return lords_day