from unittest import TestCase
import Request
import User
import datetime as dt


class TestRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp_RequestClass_tests")

    def setUp(self) -> None:
        print("setUpTestcase")

    def tearDown(self) -> None:
        print("tearDownTestcase")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown_RequestClass_tests")

    def test_get_cost(self):
        test_user = User.User("Tester", "student")
        test_request = Request.Request("request test short", 1, dt.timedelta(hours=1), "short", test_user)
        self.assertEqual(test_request.get_cost(), 60.0)
        print("function get_cost running correctly")

    def test__str__output(self):
        test_user = User.User("Tester", "student")
        test_request = Request.Request("request test short", 1, dt.timedelta(hours=1), "short", test_user)
        print("function __str__ return result" + test_request.__str__())
        self.assertEqual(test_request.__str__(), "request test short by Tester: None")

