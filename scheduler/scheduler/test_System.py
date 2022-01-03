import unittest
from unittest import TestCase
import System
from Node import *
import Constants as csts
import datetime as dt
import time


class TestSystem(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp_SystemClass_tests")

    def setUp(self) -> None:
        print("setUpTestcase")

    def tearDown(self) -> None:
        print("tearDownTestcase")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown_SystemClass_tests")

    def test_get_short_nodes(self):
        system = System.System()
        self.assertIsInstance(system.get_short_nodes(), list)
        print("function get_short_nodes() running correctly")

    def test_get_medium_nodes(self):
        system = System.System()
        self.assertIsInstance(system.get_medium_nodes(), list)
        print("function get_medium_nodes() running correctly")

    def test_get_large_nodes(self):
        system = System.System()
        self.assertIsInstance(system.get_large_nodes(), list)
        print("function get_large_nodes() running correctly")

    def test_get_gpu_nodes(self):
        system = System.System()
        self.assertIsInstance(system.get_gpu_nodes(), list)
        print("function get_get_gpu_nodes() running correctly")

    def test_next_cycle_end(self):
        test_system = System.System()
        min = dt.datetime(year=dt.MAXYEAR, month=12, day=31)
        self.assertIsInstance(test_system.next_cycle_end(min), dt.datetime)
        print("function next_cycle_end() running correctly")

    def test_is_week(self):
        test_system = System.System()
        min = dt.datetime(year=dt.MAXYEAR, month=12, day=31)
        self.assertIsInstance(test_system.is_week(min), bool)
        print("function is_week() running correctly")

    def test_get_actual_time(self):
        test_system = System.System()
        self.assertIsInstance(test_system.get_actual_time(), dt.datetime)
        print("function get_actual_time() running correctly")

    def test_get_available_time(self):
        test_system = System.System()
        self.assertIsInstance(test_system.get_available_time_short(), dt.timedelta)
        print("function get_available_time() running correctly")

    def test_get_available_nodes(self):
        test_system = System.System()
        min = dt.datetime(year=dt.MAXYEAR, month=12, day=31)
        self.assertIsInstance(test_system.get_available_nodes(min),list)
        print("function get_available_nodes() running correctly")

    def test_get_available_time_short(self):
        test_system = System.System()
        self.assertIsInstance(test_system.get_available_time_short(), dt.timedelta)
        print("function get_available_time_short() running correctly")

    def test_get_available_time_medium(self):
        test_system = System.System()
        self.assertIsInstance(test_system.get_available_time_medium(), dt.timedelta)
        print("function get_available_time_medium() running correctly")

    def test_get_available_time_large(self):
        test_system = System.System()
        self.assertIsInstance(test_system.get_available_time_large(), dt.timedelta)
        print("function get_available_time_large() running correctly")

    def test_get_available_time_gpu(self):
        test_system = System.System()
        self.assertIsInstance(test_system.get_available_time_gpu(), dt.timedelta)
        print("function get_available_time_gpu() running correctly")

    def test_get_available_nodes_short(self):
        test_system = System.System()
        min = dt.datetime(year=dt.MAXYEAR, month=12, day=31)
        self.assertIsInstance(test_system.get_available_nodes_short(min), list)
        print("get_available_nodes_short() running correctly")

    def test_get_available_nodes_medium(self):
        test_system = System.System()
        min = dt.datetime(year=dt.MAXYEAR, month=12, day=31)
        self.assertIsInstance(test_system.get_available_nodes_medium(min), list)
        print("get_available_nodes_medium() running correctly")

    def test_get_available_nodes_large(self):
        test_system = System.System()
        min = dt.datetime(year=dt.MAXYEAR, month=12, day=31)
        self.assertIsInstance(test_system.get_available_nodes_large(min), list)
        print("get_available_nodes_large() running correctly")

    def test_get_available_nodes_gpu(self):
        test_system = System.System()
        min = dt.datetime(year=dt.MAXYEAR, month=12, day=31)
        self.assertIsInstance(test_system.get_available_nodes_gpu(min), list)
        print("get_available_nodes_gpu() running correctly")

