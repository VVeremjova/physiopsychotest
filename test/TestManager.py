from admin.adminPart import Admin
from TestingWay import TestingWay
from TestingWay1 import TestingWay1
from TestingWay2 import TestingWay2

class TestManager:
     def __init__(self):
          self.data = []
          admin = Admin()          

     def ErrorsInfo(self):
          pass


     def StartTesting(self):
          "Процесс тестирования начинается здесь"          
          print "Start here"
          test_start = TestingWay()
          # do it until count of switches will not stop
          curr_shift_count = 0
          while curr_shift_count<self.admin.shift_count:
               if (getway == 1):
                    test_start = TestingWay1()
                    curr_shift_count=curr_shift_count+1
                    getway =2
                    continue
               if (getway == 2):
                    test_start = TestingWay1()
                    getway=1
                    curr_shift_count=curr_shift_count+1

          #if(TestingWay.GetUserPrintedValues()):
            #   pass

     def SumsInfo(self):
          TestingWay.CorrectOutputValues(self)
          
