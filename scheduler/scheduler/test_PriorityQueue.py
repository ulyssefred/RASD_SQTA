from unittest import TestCase
import Request
import PriorityQueue
import datetime as dt
import User


class TestPriorityQueue(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp_PriorityQueueClass_tests")

    def setUp(self) -> None:
        print("setUpTestcase")

    def tearDown(self) -> None:
        print("tearDownTestcase")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown_PriorityQueueClass_tests")

    def test_push(self):
        test_user = User.User("Tester", "student")
        test_request = Request.Request("request test short", 1, dt.timedelta(hours=1), "short", test_user)
        test_priority_queue = PriorityQueue.PriorityQueue()
        test_priority_queue.push(test_request)
        self.assertEqual(test_priority_queue.q[0], test_request)
        print("function push running correctly, request have been pushed into priority queue")

    def test_pop_priority(self):
        test_user = User.User("Tester", "student")
        test_request = Request.Request("request test short", 1, dt.timedelta(hours=1), "short", test_user)
        test_priority_queue = PriorityQueue.PriorityQueue()
        test_priority_queue.push(test_request)
        self.assertEqual(test_priority_queue.pop_priority(1, dt.timedelta(hours=1)), test_request)
        print("function pop running correctly, request have been pop from priority queue")
