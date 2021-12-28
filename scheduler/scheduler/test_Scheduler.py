from unittest import TestCase
from PriorityQueue import *
from System import *
import Scheduler
import User
import Request


class TestScheduler(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp_SchedulerClass_tests")

    def setUp(self) -> None:
        print("setUpTestcase")

    def tearDown(self) -> None:
        print("tearDownTestcase")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown_SchedulerClass_tests")

    def test_add_request(self):
        test_user = User.User("Tester", "student")
        test_request = Request.Request("request test short", 1, dt.timedelta(hours=1), "short", test_user)
        test_add_request = Scheduler.Scheduler()
        test_add_request.add_request(test_request)
        self.assertEqual(test_add_request.short_requests.q[0], test_request)
        print("Function add_request running well, modify queue correctly")

    def test_is_schedule_done(self):
        test_scheduler_is_done = Scheduler.Scheduler()
        self.assertTrue(test_scheduler_is_done.is_schedule_done())
        print("Function is_schedule_done running well, return correctly Bool value")



