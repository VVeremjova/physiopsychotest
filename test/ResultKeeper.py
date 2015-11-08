class ResultKeeper:
     _SHIFT_ERRORS = 0
     _GROUP_ERRORS = 0
     _ARITM_ERRORS = 0

     def __init__(self):
        self.data = []

     @classmethod
     def AvarageActionsInMin(self):
         TestingWay.CorrectOutputValues(self)

     @classmethod
     def AvarageActionsInMinWithShift(self):
         if(TestingWay.GetUserPrintedValues()):

      @classmethod
     def AvarageErrorsInMin(self):
         TestingWay.CorrectOutputValues(self)

     @classmethod
     def CountArithmErrors(self):
         ResultKeeper._ARITM_ERRORS= ResultKeeper._ARITM_ERRORS +1

      @classmethod
     def CountGroupWithErrors(self):
         ResultKeeper._GROUP_ERRORS= ResultKeeper._GROUP_ERRORS +1

     @classmethod
     def CountOfSumInEvery30Sec(self):
         if(TestingWay.GetUserPrintedValues()):

      @classmethod
     def CountShiftErrors(self):
         ResultKeeper._SHIFT_ERRORS= ResultKeeper._SHIFT_ERRORS +1

