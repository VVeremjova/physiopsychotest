from test.TestingWay import TestingWay


class TestingWay2(TestingWay):
     def __init__(self):
        TestingWay.__init__(self)
        self.data = []

     
     def CorrectInputValues(self):
        TestingWay._TOP_VALUE = GetTopValue()
        TestingWay._BOT_VALUE = GetBotValue()
        if(TestingWay._BOT_VALUE==GetBotInputField & TestingWay._TOP_VALUE + TestingWay._BOT_VALUE == GetTopInputField):
            TestingWay._CORRECT = TestingWay._CORRECT+1
        else:
            TestingWay._ERRORS = TestingWay._ERRORS +1
        return TestingWay._CORRECT

     
     def CorrectOutputValues(self):
         TestingWay.CorrectOutputValues(self)

     
     def CreateOutputValues(self):
        pass
         # if(TestingWay.GetUserPrintedValues()):
