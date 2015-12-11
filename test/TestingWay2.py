from test.TestingWay import TestingWay


class TestingWay2(TestingWay):
     def __init__(self):
        TestingWay.__init__(self)
        print("");

     
     @classmethod
     def CorrectInputValues(self):
        print (TestingWay._BOT_INPUT_VALUE + TestingWay2._TOP_INPUT_VALUE)
        if((TestingWay2._TOP_INPUT_VALUE==TestingWay2._TOP_VALUE) & ((TestingWay2._TOP_INPUT_VALUE + TestingWay2._BOT_INPUT_VALUE) == TestingWay2._BOT_VALUE)):
            TestingWay2._CORRECT = TestingWay2._CORRECT+1
        else:
            TestingWay2._ERRORS = TestingWay2._ERRORS +1
        return TestingWay2._CORRECT

     @classmethod
     def CorrectOutputValues(self):
         if(TestingWay2._TOP_INPUT_VALUE!=TestingWay2._OLD_TOP_VALUE & TestingWay2._BOT_INPUT_VALUE!= TestingWay2._OLD_BOT_VALUE):
             return "diff"
         else:
             return "same"

     
     def CreateOutputValues(self):
        pass
         # if(TestingWay.GetUserPrintedValues()):
