# -*- coding: cp1251 -*-
from test.ResultKeeper import ResultKeeper
class FormatResult:
    def __init__(self):
        pass
        #self.format_string=""+str(result.SustainedAttention())

    def getAllResults(self):
        result = ResultKeeper()
        self.format_string = "Результаты: \n"+\
        "Число подсчитанных сумм: \n"+\
        "Число ошибок: \n" +\
        "Устойчивость переключения внимания: \n" +\
        "Степень переключаемости внимания: "+str(result.SustainedAttention())+\
        "\n"
        
    def fresult(self):
        self.getAllResults()
        return self.format_string
    
