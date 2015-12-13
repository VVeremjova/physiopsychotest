from TestingWay import TestingWay


class TestingWay1(TestingWay):
     def __init__(self):
        TestingWay.__init__(self)
        print("");


     @classmethod
     def CorrectInputValues(self):
        print (TestingWay._BOT_INPUT_VALUE + TestingWay._TOP_INPUT_VALUE)
        if((TestingWay._BOT_INPUT_VALUE==TestingWay._BOT_VALUE) & ((TestingWay._TOP_INPUT_VALUE + TestingWay._BOT_INPUT_VALUE) == TestingWay._TOP_VALUE)):
            TestingWay._CORRECT = TestingWay._CORRECT+1
        else:
            if((TestingWay._TOP_INPUT_VALUE==TestingWay._TOP_VALUE) & ((TestingWay._TOP_INPUT_VALUE + TestingWay._BOT_INPUT_VALUE) == TestingWay._BOT_VALUE)):
                TestingWay._ERRORS_WAY = TestingWay._ERRORS_WAY+1
            else:
                TestingWay._ERRORS_VAL = TestingWay._ERRORS_VAL +1


     @classmethod
     def CorrectOutputValues(self):
         if(TestingWay._TOP_INPUT_VALUE!=TestingWay._OLD_TOP_VALUE & TestingWay._BOT_INPUT_VALUE!= TestingWay._OLD_BOT_VALUE):
             return "diff"
         else:
             return "same"


     def CreateOutputValues(self):
        pass
         # if(TestingWay.GetUserPrintedValues()):
