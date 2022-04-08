import mockito
import unittest

from listPR import *

class HelloWorldTest(unittest.TestCase):
    def test_should_return_all_prs(self):
        out = mockito.mock()
        getPRoutput()
        mockito.verify().write("Repo_Url:git://github.com/avimishra016/pullrequeststats.git")