import random


class TestingWay:
    _CORRECT = 0
    _ERRORS  = 0
    _TOP_VALUE = 0
    _BOT_VALUE = 0
    _OLD_TOP_VALUE = 0
    _OLD_BOT_VALUE = 0

    def __init__(self):
        pass

    @classmethod
    def CountCorrectSums(self):
        return TestingWay._CORRECT

    @classmethod
    def CountErrors(self):
        return TestingWay._ERRORS

    @classmethod
    def CorrectInputValues(self):
        return TestingWay._CORRECT

    @classmethod
    def CorrectOutputValues(self):
        return TestingWay._CORRECT

    @classmethod
    def GetRandomNumbers(self):
        return random.randint(0,9)

    @classmethod
    def GetUserPrintedValues(self):
        TestingWay._OLD_TOP_VALUE = TestingWay._TOP_VALUE
        TestingWay._OLD_BOT_VALUE = TestingWay._BOT_VALUE
        TestingWay._TOP_VALUE = GetTopInputValue()
        TestingWay._BOT_VALUE = GetBotInputValue()
        return 1
