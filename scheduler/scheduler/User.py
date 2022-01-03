import Request
import Constants as csts
import datetime as dt


class User:
    def __init__(self, user_name, user_type, credit = None):
        """
        Initializes the user with a number of allocated credits for the use of the HPC
        :param user_name: a string
        :param user_type: a string
        :param credit: an integer
        """
        self.user_name = user_name
        self.user_type = user_type
        # new user_type check code
        if user_type not in ["student", "researcher", "it_support"]:
            raise Exception("Input invalid user_type")

        if credit is None:
            if user_type == "student":
                self.credit = 50000
            if user_type == "researcher":
                self.credit = 100000
            if user_type == "it_support":
                self.credit = 0
        else:
            self.credit = credit

    def create_request(self, title: str, nbr_nodes: int, time: int, req_type: str) -> Request.Request:
        """
        Return a request object corresponding to the chosen characteristics
        :param title: a string (name of the task)
        :param nbr_nodes: an integer (corresponding to the number of nodes required)
        :param time: an integer (corresponding to the number of hours required for the task)
        :param req_type: a string (corresponding to the type of the task)
        :return: a request object
        """
        cost = 0
        # new req_type check code
        if req_type not in ["short", "medium", "large", "huge", "gpu"]:
            raise ValueError("Input invalid request type")

        if req_type == "gpu":
            cost += time * csts.COST_HOUR_GPU * nbr_nodes
        else:
            cost += time * csts.COST_HOUR_CPU * nbr_nodes
        # if self.credit < cost:
        #     print(cost, "is above the remaining credit of the user.")
        if cost < 0:
            raise ValueError("Cost cannot be below 0.")
        self.credit -= cost
        if self.credit < 0:
            return Request.Request("Insufficient balance", nbr_nodes, dt.timedelta(hours=time), req_type, self)
        return Request.Request(title, nbr_nodes, dt.timedelta(hours=time), req_type, self)
