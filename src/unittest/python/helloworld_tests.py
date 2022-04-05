import mockito
import unittest

from helloworld import helloworld

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mockito.mock()

        helloworld(out)

        mockito.verify(out).write("Hello world of Python\n")