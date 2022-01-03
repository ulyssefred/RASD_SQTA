import unittest
from scheduler.scheduler import HTMLTestRunner
import time


if __name__ == '__main__':
    """
    Find the test case file under the current directory
    """
    testSuit = unittest.TestLoader().discover('.')
    filename = "C:\\Users\\ulysses\\PycharmProjects\\RASD_SQTA\\html_test_file.html".\
        format(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is an unittest report', description= None)
        runner.run(testSuit)