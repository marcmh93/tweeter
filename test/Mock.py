import unittest
from src.tweeter import *
from mock import Mock



class twiitTest(unittest.TestCase):
    def test1(self):
        Mock_tweet = Mock()
        tweeter.twiit(Mock_tweet, "Test1")
        Mock_tweet.PostUpdate.assert_called_with("msg")

    def tes2(self):
        Mock_tweet = Mock()
        tweeter.twiit(Mock_tweet, "Test2")
        Mock_tweet.PostUpdate.assert_called_with("msg")


if __name__ == '__main__':
    unittest.main()