

from test.TestingWay import TestingWay


class TestingWay1(TestingWay):
     def __init__(self):
        TestingWay.__init__(self)
        self.data = []

     def CorrectInputValues(self):
        TestingWay._TOP_VALUE = GetTopValue()
        TestingWay._BOT_VALUE = GetBotValue()
        if(TestingWay._TOP_VALUE==GetTopInputField & TestingWay._TOP_VALUE + TestingWay._BOT_VALUE == GetBotInputField):
            TestingWay._CORRECT = TestingWay._CORRECT+1
        else:
            TestingWay._ERRORS = TestingWay._ERRORS +1
        return TestingWay._CORRECT

     def CorrectOutputValues(self):
         if(TestingWay._TOP_VALUE!=TestingWay._OLD_TOP_VALUE & TestingWay._BOT_VALUE!= TestingWay._OLD_BOT_VALUE):
             return 1
         else:
             return 2

     def CreateOutputValues(self):
        pass
         # if(TestingWay.GetUserPrintedValues()):
