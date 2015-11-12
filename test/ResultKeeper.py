class ResultKeeper:
     """Keep all testing results,
     including errors, count of sum,
     all information, that can be get from tests """
     _SHIFT_ERRORS = 0
     _GROUP_ERRORS = 0
     _ARITM_ERRORS = 0
     _TIME_ERROR = False

     def __init__(self):
        self.data = []

     def AvarageActionsInMin(self):
          TestingWay.CorrectOutputValues(self)

     def AvarageActionsInMinWithShift(self):
          #if(TestingWay.GetUserPrintedValues()):
          pass
               

     def AvarageErrorsInMin(self):
          #TestingWay.CorrectOutputValues(self)
          pass

     def CountArithmErrors(self):
          ResultKeeper._ARITM_ERRORS= ResultKeeper._ARITM_ERRORS +1

     def CountGroupWithErrors(self):
          ResultKeeper._GROUP_ERRORS= ResultKeeper._GROUP_ERRORS +1

     def CountOfSumInEvery30Sec(self):
          if(TestingWay.GetUserPrintedValues()):
               pass

     def CountShiftErrors(self):
          ResultKeeper._SHIFT_ERRORS = ResultKeeper._SHIFT_ERRORS +1

     def SustainedAttention(self):
          return 1