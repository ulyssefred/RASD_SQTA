import datetime as dt


class Node:
    def __init__(self, is_gpu=False):
        """
        Initializes a node with a starting time using get_next_day and a list of requests for this node
        :param is_gpu: a boolean
        """
        self.is_gpu = is_gpu
        self.available_time = self._get_next_day()
        self.list_of_requests =[]

    def _get_next_day(self):
        """
        Return a datetime object that corresponds to midnight of the day when the program is computed
        :return: a datetime object
        """
        year = dt.datetime.now().year
        month = dt.datetime.now().month
        day = dt.datetime.now().day
        return dt.datetime(year, month, day)+dt.timedelta(days=1)

    def add_request(self, request, actual_time):
        """
        Add a request to that node at actual_time
        :param request: a request object
        :param actual_time: a datetime object
        :return: Nothing
        """
        self.list_of_requests.append(request)
        self.available_time = actual_time + request.req_time