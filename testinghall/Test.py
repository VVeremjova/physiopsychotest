from test.TestingWay2 import TestingWay2
from test.TestingWay import TestingWay
from start import startTesting


class Test():
     _TOP_INPUT_VALUE = 0
     _BOT_INPUT_VALUE = 0
     _OLD_TOP_VALUE = 0
     _OLD_BOT_VALUE = 0
     _CORRECT = 0
     _ERRORS  = 0
     _TOP_VALUE = 0
     _BOT_VALUE = 0


     def __init__(self):
        print("Test 1")
        var=1
        while var ==1:
            TestingWay.GetRandomNumbers("T")
            TestingWay.GetRandomNumbers("B")
            print("Top value : " + Test._TOP_INPUT_VALUE.__str__())
            print ("Bot value : " + Test._BOT_INPUT_VALUE.__str__())
            print TestingWay2.CorrectOutputValues()
            print TestingWay2.CorrectInputValues()

startTesting()

