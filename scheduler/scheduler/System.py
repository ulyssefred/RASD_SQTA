import datetime as dt
from Node import *
import Constants as csts


class System:
    def __init__(self):
        """
        Initializes the system by creating the correct number of nodes
        """
        self.nodes = []
        for i in range(csts.NBR_NODES_CPU):
            self.nodes.append(Node(False))
        for i in range(csts.NBR_NODES_GPU):
            self.nodes.append(Node(True))

    def get_short_nodes(self):
        """
        Return the nodes corresponding to the short tasks
        :return: a list of nodes
        """
        return self.nodes[csts.INDEX_NODES_SHORT:csts.INDEX_NODES_MEDIUM]

    def get_medium_nodes(self):
        """
        Return the nodes corresponding to the medium tasks
        :return: a list of nodes
        """
        return self.nodes[csts.INDEX_NODES_MEDIUM:csts.INDEX_NODES_LARGE]

    def get_large_nodes(self):
        """
        Return the nodes corresponding to the large tasks
        :return: a list of nodes
        """
        return self.nodes[csts.INDEX_NODES_LARGE:csts.NBR_NODES_CPU]

    def get_gpu_nodes(self):
        """
        Return the nodes corresponding to the gpu tasks
        :return: a list of nodes
        """
        return self.nodes[csts.NBR_NODES_CPU:]

    def next_cycle_end(self, timestamp):
        """
        Calculate the next time from timestamp when the system switch between huge tasks and others
        :param timestamp: a datetime object
        :return: a datetime object
        """
        fromstartweek = dt.timedelta(days=timestamp.weekday(), hours=timestamp.hour)
        if fromstartweek < dt.timedelta(hours=9):
            return timestamp - fromstartweek + dt.timedelta(hours=9)
        elif fromstartweek < dt.timedelta(days=4, hours=17):
            return timestamp - fromstartweek + dt.timedelta(days=4, hours=17)
        else:
            return timestamp - fromstartweek + dt.timedelta(days=7, hours=9)

    def is_week(self, timestamp):
        """
        Return True if timestamp is during the week cycle, False otherwise
        :param timestamp: a datetime object
        :return: a boolean
        """
        fromstartweek = dt.timedelta(days=timestamp.weekday(), hours=timestamp.hour)
        if fromstartweek < dt.timedelta(hours=9):
            return False
        elif fromstartweek < dt.timedelta(days=4, hours=17):
            return True
        else:
            return False

    def get_actual_time(self):
        """
        Return a datetime object representing the next time a node is available
        :return: a datetime object
        """
        min = dt.datetime(year= dt.MAXYEAR, month= 12, day= 31)
        for node in self.nodes:
            if node.available_time < min:
                min = node.available_time
        return min

    def get_available_time(self, timestamp=None):
        """
        Return the timedelta of available time with nodes between timestamp and the next switch of cycle
        If timestamp is not defined, it is set to the next datetime when a node is available

        :param timestamp: a datetime object
        :return: a timedelta object
        """
        if timestamp is None:
            timestamp = self.get_actual_time()
        min = self.get_actual_time() if self.get_actual_time() > timestamp else timestamp
        return self.next_cycle_end(min) - min

    def get_available_nodes(self, timestamp):
        """
        Return the number of nodes available at timestamp
        :param timestamp: a datetime object
        :return: an integer
        """
        count = []
        for node in self.nodes:
            if node.available_time <= timestamp:
                count.append(node)
        return count

    def get_available_time_short(self, timestamp=None):
        """
        Return the timedelta of available time with nodes between timestamp and the next switch of cycle for short tasks
        If timestamp is not defined, it is set to the next datetime when a node is available

        :param timestamp: a datetime object
        :return: a timedelta object
        """
        if timestamp is None:
            timestamp = self.get_actual_time()
        min = dt.datetime(year= dt.MAXYEAR, month= 12, day= 31)
        for node in self.get_short_nodes():
            if node.available_time < min:
                min = node.available_time
        min = min if min > timestamp else timestamp
        return self.next_cycle_end(min) - min

    def get_available_time_medium(self, timestamp=None):
        """
        Return the timedelta of available time with nodes between timestamp and the next switch of cycle for medium
        tasks
        If timestamp is not defined, it is set to the next datetime when a node is available

        :param timestamp: a datetime object
        :return: a timedelta object
        """
        if timestamp is None:
            timestamp = self.get_actual_time()
        min = dt.datetime(year= dt.MAXYEAR, month= 12, day= 31)
        for node in self.get_medium_nodes():
            if timestamp < node.available_time < min:
                min = node.available_time
        min = min if min > timestamp else timestamp
        return self.next_cycle_end(min) - min

    def get_available_time_large(self, timestamp=None):
        """
        Return the timedelta of available time with nodes between timestamp and the next switch of cycle for large tasks
        If timestamp is not defined, it is set to the next datetime when a node is available

        :param timestamp: a datetime object
        :return: a timedelta object
        """
        if timestamp is None:
            timestamp = self.get_actual_time()
        min = dt.datetime(year= dt.MAXYEAR, month= 12, day= 31)
        for node in self.get_large_nodes():
            if timestamp < node.available_time < min:
                min = node.available_time
        min = min if min > timestamp else timestamp
        return self.next_cycle_end(min) - min

    def get_available_time_gpu(self,timestamp = None):
        """
        Return the timedelta of available time with nodes between timestamp and the next switch of cycle for gpu tasks
        If timestamp is not defined, it is set to the next datetime when a node is available

        :param timestamp: a datetime object
        :return: a timedelta object
        """
        if timestamp is None:
            timestamp = self.get_actual_time()
        min = dt.datetime(year= dt.MAXYEAR, month= 12, day= 31)
        for node in self.get_gpu_nodes():
            if timestamp < node.available_time < min:
                min = node.available_time
        min = min if min > timestamp else timestamp
        return self.next_cycle_end(min) - min

    def get_available_nodes_short(self, timestamp):
        """
        Return the number of nodes available at timestamp for short tasks
        :param timestamp: a datetime object
        :return: an integer
        """
        count = []
        for node in self.get_short_nodes():
            if node.available_time <= timestamp:
                count.append(node)
        return count

    def get_available_nodes_medium(self, timestamp):
        """
        Return the number of nodes available at timestamp for medium tasks
        :param timestamp: a datetime object
        :return: an integer
        """
        count = []
        for node in self.get_medium_nodes():
            if node.available_time <= timestamp:
                count.append(node)
        return count

    def get_available_nodes_large(self, timestamp):
        """
        Return the number of nodes available at timestamp for large tasks
        :param timestamp: a datetime object
        :return: an integer
        """
        count = []
        for node in self.get_large_nodes():
            if node.available_time <= timestamp:
                count.append(node)
        return count

    def get_available_nodes_gpu(self, timestamp):
        """
        Return the number of nodes available at timestamp for gpu tasks
        :param timestamp: a datetime object
        :return: an integer
        """
        count = []
        for node in self.get_gpu_nodes():
            if node.available_time <= timestamp:
                count.append(node)
        return count

