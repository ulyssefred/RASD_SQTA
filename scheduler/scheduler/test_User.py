import unittest
import User
import Request
import Constants as csts
import datetime as dt


class UnittestUserCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp_UserClass_tests")

    def setUp(self) -> None:
        print("setUpTestcase")

    def tearDown(self) -> None:
        print("tearDownTestcase")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown_UserClass_tests")

    def test_User_init_01(self):
        user = User.User("Tester", "student")
        self.assertEqual(user.user_name, "Tester")
        self.assertEqual(user.user_type, "student")
        self.assertEqual(user.credit, 40320)
        print("Successfully creating the correct user: Tester, student, credit : 40320.")

    def test_User_init_02(self):
        user = User.User("Tester", "researcher")
        self.assertEqual(user.user_name, "Tester")
        self.assertEqual(user.user_type, "researcher")
        self.assertEqual(user.credit, 483840)
        print("Successfully creating the correct user: Tester, researcher, credit : 483840.")

    def test_User_init_03(self):
        user = User.User("Tester", "it_support")
        self.assertEqual(user.user_name, "Tester")
        self.assertEqual(user.user_type, "it_support")
        self.assertEqual(user.credit, 5806080)
        print("Successfully creating the correct user: Tester, it_support, credit : 5806080.")

    def test_User_init_04(self):
        user = User.User("Tester", "student", 400)
        self.assertEqual(user.user_name, "Tester")
        self.assertEqual(user.user_type, "student")
        self.assertEqual(user.credit, 400)
        print("Successfully creating the correct user: Tester, student, credit : 400.")

    def test_User_init_05(self):
        self.assertRaisesRegex(Exception, "Input invalid user_type", User.User, "Tester", "PHD")
        print("Successfully raise invalid user_type exception")

    def test_User_Creat_request01(self):
        user = User.User("Tester", "student", 400)
        self.assertIsInstance(user.create_request("request test short", 1, 3, "short"), Request.Request)
        print("Successfully created request")

    def test_User_Creat_request02(self):
        user = User.User("Tester", "student", 0)
        self.assertIsInstance(user.create_request("request test short", 1, 3, "gpu"), Request.Request)
        self.assertEqual(user.credit, -3 * csts.COST_HOUR_GPU * 1)
        print("Successfully created request with gpu")

    def test_User_Creat_request03(self):
        user = User.User("Tester", "student", 400)
        self.assertRaisesRegex(ValueError, "Input invalid request type", user.create_request, "request test short"
                               , 1, 3, "ggg")
        print("Successfully raise invalid request type exception")


