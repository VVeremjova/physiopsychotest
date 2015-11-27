from admin.adminPart import Admin
from TestingWay import TestingWay
from TestingWay1 import TestingWay1
from TestingWay2 import TestingWay2
from ResultKeeper import ResultKeeper

class TestManager:
     "Manager all accesses to testing\
     part, get logic of switches between \
     different way of testing"
     def __init__(self):
          self.data = []
          admin = Admin()        
          result = ResultKeeper()  
          curr_shift_count = 0

     def ErrorsInfo(self):
          pass


     def StartTesting(self):
          "Testing process"          
          print "Start here"          
          # do it until count of switches will not stop  
          test_start_1way = TestingWay1()   
          test_start_2way = TestingWay2()           
          # while not isTestingFinished():
               # if (getway == 1):
               #      res = test_start_1way.Start()
               #      if res == false:
               #           break
               #      self.curr_shift_count=self.curr_shift_count+1
               #      getway =2
               #      continue
               # if (getway == 2):
               #      res = test_start_2way.Start()
               #      if res == false:
               #           break
               #      getway=1
               #      self.curr_shift_count=self.curr_shift_count+1

     def isTestingFinished(self):
          "return true if all conditions are satisfied"
          if self.curr_shift_count <self.admin.shift_count:
               return false
          return true


     def SumsInfo(self):
         pass
          
