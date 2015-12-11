import random
import time
from ResultKeeper import ResultKeeper
from admin.adminPart import Admin

class TestingWay:
    "Keep actions that the same to both ways of testing"
    _CORRECT = 0
    _ERRORS  = 0
    _TOP_VALUE = 0
    _BOT_VALUE = 0
    _OLD_TOP_VALUE = 0
    _OLD_BOT_VALUE = 0
    _TOP_INPUT_VALUE = 0
    _BOT_INPUT_VALUE = 0

    def __init__(self):
        _CORRECT = 0
        _ERRORS  = 0
        _TOP_VALUE = 0
        _BOT_VALUE = 0
        _OLD_TOP_VALUE = 0
        _OLD_BOT_VALUE = 0
        result_keeper = ResultKeeper()
        current_testing_time = 0


    def CountCorrectSums(self):
        return self._CORRECT

    def CountErrors(self):
        return self._ERRORS

    def CorrectInputValues(self):
        "will be overriden"
        pass
        # return self._CORRECT

    def CorrectOutputValues(self):
        "will be overriden"
        pass
        # return self._CORRECT

    @classmethod
    def GetTopInputValue(self, value):
        return value


    @classmethod
    def GetTopValue(self):
       user_input = input("Input Top value please: ")
       return user_input

    @classmethod
    def GetBotValue(self):
       user_input = input("Input Bot Value please: ")
       return  user_input

    @classmethod
    def CreateOutputValues(self):
        return 0

    @classmethod
    def GetTopInputField(self):
       return TestingWay._CORRECT

    @classmethod
    def GetBotInputField(self):
       return TestingWay._CORRECT

    @classmethod
    def CountCorrectSums(self):
       return TestingWay._CORRECT

    @classmethod
    def CountErrors(self):
       return TestingWay._ERRORS

    @classmethod
    def GetBotInputValue(self, value):
        return value

    @classmethod
    def GetRandomNumbers(self, code):
        a= random.randint(0,9)
        if(code == "T"):
            TestingWay._TOP_INPUT_VALUE = a
        else:
            TestingWay._BOT_INPUT_VALUE = a
        return a


    def GetUserPrintedValues(self):
        self._OLD_TOP_VALUE = self._TOP_VALUE
        self._OLD_BOT_VALUE = self._BOT_VALUE
        #self._TOP_VALUE = GetTopInputValue()
        #self._BOT_VALUE = GetBotInputValue()
        return 1

    def OutOfTime(self,currtime):
        if currtime>self.admin.time_answer:
            # from result keeper 
            self.result_keeper._TIME_ERROR = True
            return False
        return True    

    def Start(self):
        "Starting testing"
        #start timing
       # while not StopCurrTestWay():
        #    currtime1 = time.clock()
         #   GetUserPrintedValues(self)
        #    currtime = time.clock() - currtime1
        #    if OutOfTime(currtime):
        #        print "ERROR. Get time out"
        #        return False

            ################
            #CorrectInputValues()
            #CreateOutputValues()
            #CorrectOutputValues()
            #################


        return True

    def StopCurrTestWay(self):
        "When testing should be stopped and we need shift"
        #if current_testing_time < self.admin.time_change_shifting:
        #    return False
        return True
