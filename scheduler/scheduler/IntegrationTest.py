from Scheduler import *
import User
import random
from unittest import TestCase


class TestRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Integration testing")

    def setUp(self) -> None:
        print("setUpTest")

    def tearDown(self) -> None:
        print("tearDownTest")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Integration testing end")

    """
    Integration testing
    """
    user_names = ["Xiao Wen", "Lucas Pin-Belloc", "Papa Dafoor", "Charles Lefever", "Jun Lin", "Irene Moulitsas"]
    user_types = ["student", "student", "student", "student", "researcher", "researcher"]
    users = []
    requests = []
    for i in range(len(user_names)):
        users.append(User.User(user_names[i], user_types[i]))
    for user in users:
        for n in range(10):
            r = random.randint(0,4)
            if r == 0:
                time = 1 if random.random() < 0.75 else 2
                nodes = 1 if random.random() < 0.67 else 2
                requests.append(user.create_request("request "+str(n)+" short",nodes,time,"short"))
            if r == 1:
                time = 8
                nodes = random.randint(0, 4)  + random.randint(0, 4)
                requests.append(user.create_request("request "+str(n)+" medium", nodes, time, "medium"))
            if r == 2:
                time = 8 + random.randint(0, 4) + random.randint(0, 4)
                nodes = random.randint(1, 32) + random.randint(1, 32)
                requests.append(user.create_request("request "+str(n)+" large", nodes, time, "large"))
            if r == 3:
                time = random.randint(1, 16)
                nodes = random.randint(1,8)
                requests.append(user.create_request("request "+str(n)+" gpu", nodes, time, "gpu"))
            if r == 4:
                nodes = None
                time = None
                if random.random() < 0.5:
                    nodes = 64 + random.randint(1, 32) + random.randint(1, 32)
                    time = random.randint(1, 24)
                else:
                    nodes = random.randint(1, 32) + random.randint(1, 32)
                    time = 24 + random.randint(1, 24)
                requests.append(user.create_request("request "+str(n)+" huge", nodes, time, "huge"))
    scheduler = Scheduler()
    for req in requests:
        scheduler.add_request(req)
    scheduler.schedule()
    for req in requests:
        print(req)
    print(scheduler.actual_time)