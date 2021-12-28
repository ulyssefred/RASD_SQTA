from PriorityQueue import *
from System import *


class Scheduler:
    def __init__(self):
        """
        Initializes the different queues of the scheduler
        """
        self.short_requests = PriorityQueue()
        self.medium_requests = PriorityQueue()
        self.large_requests = PriorityQueue()
        self.gpu_requests = PriorityQueue()
        self.huge_requests = PriorityQueue()
        self.system = System()
        self.actual_time = self.system.get_actual_time()

    def add_request(self, request):
        """
        Adds a request to the corresponding queue in the scheduler

        :param request: Request object containing a new request
        :return: Nothing
        """
        if request.req_type == "short":
            self.short_requests.push(request)
        elif request.req_type == "medium":
            self.medium_requests.push(request)
        elif request.req_type == "large":
            self.large_requests.push(request)
        elif request.req_type == "huge":
            self.huge_requests.push(request)
        elif request.req_type == "gpu":
            self.gpu_requests.push(request)

    def is_schedule_done(self):
        """
        Checks whether the scheduling has been done

        :return: Nothing
        """
        is_short_schedule_done = len(self.short_requests.q) == 0
        is_medium_schedule_done = len(self.medium_requests.q) == 0
        is_large_schedule_done = len(self.large_requests.q) == 0
        is_gpu_schedule_done = len(self.gpu_requests.q) == 0
        is_huge_schedule_done = len(self.huge_requests.q) == 0
        return is_huge_schedule_done and is_gpu_schedule_done and is_large_schedule_done and is_medium_schedule_done and is_short_schedule_done

    def schedule(self):
        """
        Schedules the different tasks on the different nodes

        :return: Nothing
        """
        while not self.is_schedule_done():
            if self.system.is_week(self.actual_time):
                if len(self.short_requests.q) != 0:
                    nodes = self.system.get_available_nodes_short(self.actual_time)
                    time_available = self.system.get_available_time_short(self.actual_time)
                    res = self.short_requests.pop_priority(len(nodes),time_available)
                    if res:
                        res.time_of_computation = self.actual_time
                        for i in range(res.nbr_nodes):
                            nodes[i].add_request(res, self.actual_time)
                if len(self.medium_requests.q) != 0:
                    nodes = self.system.get_available_nodes_medium(self.actual_time)
                    time_available = self.system.get_available_time_medium(self.actual_time)
                    res = self.medium_requests.pop_priority(len(nodes),time_available)
                    if res:
                        res.time_of_computation = self.actual_time
                        for i in range(res.nbr_nodes):
                            nodes[i].add_request(res, self.actual_time)
                if len(self.large_requests.q) != 0:
                    nodes = self.system.get_available_nodes_large(self.actual_time)
                    time_available = self.system.get_available_time_large(self.actual_time)
                    res = self.large_requests.pop_priority(len(nodes),time_available)
                    if res:
                        res.time_of_computation = self.actual_time
                        for i in range(res.nbr_nodes):
                            nodes[i].add_request(res, self.actual_time)
                if len(self.gpu_requests.q) != 0:
                    nodes = self.system.get_available_nodes_gpu(self.actual_time)
                    time_available = self.system.get_available_time_gpu(self.actual_time)
                    res = self.gpu_requests.pop_priority(len(nodes),time_available)
                    if res:
                        res.time_of_computation = self.actual_time
                        for i in range(res.nbr_nodes):
                            nodes[i].add_request(res, self.actual_time)
                if self.actual_time >= self.system.get_actual_time():
                    self.actual_time += dt.timedelta(hours=1)
                else:
                    self.actual_time = self.system.get_actual_time()
            else:
                if len(self.huge_requests.q) != 0:
                    nodes = self.system.get_available_nodes(self.actual_time)
                    time_available = self.system.get_available_time(self.actual_time)
                    res = self.huge_requests.pop_priority(len(nodes),time_available)
                    if res:
                        res.time_of_computation = self.actual_time
                        for i in range(res.nbr_nodes):
                            nodes[i].add_request(res, self.actual_time)
                if self.actual_time >= self.system.get_actual_time():
                    self.actual_time += dt.timedelta(hours=1)
                else:
                    self.actual_time = self.system.get_actual_time()
