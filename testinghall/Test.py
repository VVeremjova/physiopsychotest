import random


class Test():


     _CORRECT = 0
     _ERRORS  = 0
     _TOP_VALUE = 0
     _BOT_VALUE = 0
     _TOP_INPUT_VALUE = 0
     _BOT_INPUT_VALUE = 0
     _OLD_TOP_VALUE = 0
     _OLD_BOT_VALUE = 0


     def __init__(self):
        print("Test 1");
        var=1
        while var ==1:
            Test.GetRandomNumbers("T")
            Test.GetRandomNumbers("B")
            print("Top value : " + Test._TOP_INPUT_VALUE.__str__())
            print ("Bot value : " + Test._BOT_INPUT_VALUE.__str__())
            print (Test.CorrectOutputValues())
            print  Test.CorrectInputValues()


     @classmethod
     def GetTopValue(self):
        user_input = input("Input Top value please: ")
        return user_input

     @classmethod
     def GetBotValue(self):
        user_input = input("Input Bot Value please: ")
        return  user_input

     @classmethod
     def CorrectInputValues(self):
        Test._TOP_VALUE = Test.GetTopValue()
        Test._BOT_VALUE = Test.GetBotValue()
        print (Test._TOP_VALUE)
        print (Test._BOT_INPUT_VALUE + Test._TOP_INPUT_VALUE)
        print (Test._BOT_VALUE)
        if((Test._TOP_INPUT_VALUE==Test._TOP_VALUE) & ((Test._TOP_INPUT_VALUE + Test._BOT_INPUT_VALUE) == Test._BOT_VALUE)):
            Test._CORRECT = Test._CORRECT+1
        else:
            Test._ERRORS = Test._ERRORS +1
        return Test._CORRECT

     @classmethod
     def CorrectOutputValues(self):
         if(Test._TOP_INPUT_VALUE!=Test._OLD_TOP_VALUE & Test._BOT_INPUT_VALUE!= Test._OLD_BOT_VALUE):
             return 1
         else:
             return 2

     @classmethod
     def CreateOutputValues(self):
         return 0

     @classmethod
     def GetTopInputField(self):
        return Test._CORRECT

     @classmethod
     def GetBotInputField(self):
        return Test._CORRECT

     @classmethod
     def CountCorrectSums(self):
        return Test._CORRECT

     @classmethod
     def CountErrors(self):
        return Test._ERRORS

     @classmethod
     def GetRandomNumbers(self, code):
        a= random.randint(0,9)
        if(code == "T"):
            Test._TOP_INPUT_VALUE = a
        else:
            Test._BOT_INPUT_VALUE = a


     @classmethod
     def GetUserPrintedValues(self):
        Test._OLD_TOP_VALUE = Test._TOP_VALUE
        Test._OLD_BOT_VALUE = Test._BOT_VALUE

        return 1

x = Test()