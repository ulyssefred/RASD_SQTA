import datetime
from unittest import TestCase
import Node
import Request
import datetime as dt
import User


class TestNode(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp_NodeClass_tests")

    def setUp(self) -> None:
        print("setUpTestcase")

    def tearDown(self) -> None:
        print("tearDownTestcase")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown_NodeClass_tests")

    def test__get_next_day(self):
        test_node = Node.Node()
        year = dt.datetime.now().year
        month = dt.datetime.now().month
        day = dt.datetime.now().day
        self.assertEqual(test_node._get_next_day(), dt.datetime(year, month, day)+dt.timedelta(days=1))
        print("Get next day successfully")

    def test_add_request(self):
        test_user = User.User("Tester", "student")
        test_request = Request.Request("request test short", 1, dt.timedelta(hours=1), "short", test_user)
        actual_time = datetime.datetime.now()
        test_node = Node.Node()
        test_node.add_request(test_request,actual_time)
        self.assertEqual(test_node.list_of_requests[0], test_request)
        self.assertEqual(test_node.available_time, actual_time + test_request.req_time)
        print("Modify request lists and available time successfully")

