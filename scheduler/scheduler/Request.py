import Constants as csts


class Request:
    def __init__(self, title, nbr_nodes, req_time, req_type, user):
        """
        Initialize a request with the different characteristics chosen
        :param title: a string (Name of the task)
        :param nbr_nodes: an integer (Number of nodes required to handle this task)
        :param req_time: a timedelta (Time to achieve this task)
        :param req_type: a string (Type of request)
        :param user: a user object (User which created this task)
        """
        self.title = title
        self.nbr_nodes = nbr_nodes
        self.req_time = req_time
        self.req_type = req_type
        self.user = user
        self.time_of_computation = None

    def get_cost(self):
        """
        Return the cost of the task
        :return: an integer
        """
        duration = self.req_time.days * 24 + self.req_time.seconds / 3600
        if self.req_type == "gpu":
            return duration * csts.COST_HOUR_GPU * self.nbr_nodes
        return duration * csts.COST_HOUR_CPU * self.nbr_nodes

    def __str__(self):
        """
        To print this task and all of it's important details
        :return: a string
        """
        return self.title + " by " + self.user.user_name + ": " + str(self.time_of_computation)