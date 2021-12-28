class PriorityQueue:
    def __init__(self):
        """
        Initialize an empty priority queue
        """
        self.q = []

    def push(self, request):
        """
        Add a request to the priority queue
        :param request: a request object
        :return: Nothing
        """
        self.q.append(request)

    def pop_priority(self, available_nodes, remaining):
        """
        Get a request that fits the characteristics defined by the parameters
        :param available_nodes: an integer (Number of available nodes at this time)
        :param remaining: a timedelta object (Time that is left before the next cycle)
        :return: Either a request or the boolean False if there is no corresponding request
        """
        for i in range(len(self.q)):
            if self.q[i].req_time <= remaining:
                if self.q[i].nbr_nodes <= available_nodes:
                    result = self.q[i]
                    del self.q[i]
                    return result
        return False
