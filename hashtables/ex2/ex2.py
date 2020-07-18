#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    this_trip = [None] * length
    this_flights = {}
    for ticket in tickets:
        if ticket.source == 'NONE':
            this_trip[0] = ticket.destination
        this_flights[ticket.source] = ticket.destination

    for index in range(1, length):
        source = this_trip[index-1]
        this_trip[index] = this_flights[source]

    return this_trip


t1 = Ticket("NONE", "PHX")
t2 = Ticket("PHX", "POR")
t3 = Ticket("POR", "NONE")

tickets = [t1, t2, t3]

print(reconstruct_trip(tickets, 3))
