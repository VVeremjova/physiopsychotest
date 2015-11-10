# -*- coding: cp1251 -*-
import PrintAndSave
class Admin():
    "Get and set information about all values that are using in testing"
    # default values
    # поле времени ввода ответа во время тестирования (sec)
    # time_answer = 2
    # количество смен переключений (sec)
    # shift_count = 5
    # время смены способа тестирования (sec)
    # time_change_shifting = 30
    
    def __init__(self, time_answer = 2,
                 shift_count = 5, time_change_shifting = 30):
        self.time_answer = time_answer
        self.shift_count = shift_count
        self.time_change_shifting = time_change_shifting
    
    def set_time_answer(self, time_answer):
        self.time_answer = time_answer

    def set_shift_count(self, shift_count):
        self.shift_count = shift_count

    def set_time_change_shifting(self, time_change_shifting):
        self.time_change_shifting = time_change_shifting

    def save_in_file(self, value = True):
        self.save_in_file = value

    def print_result(self, print_result = True):
        self.print_result = print_result
        
    def format_string(self, formats=None):
        self.format_strings = formats

    def set_filename(self, filename):
        self.filename = filename

    def save_results(self, results = None):
        print self.format_strings
        printsave = PrintAndSave.PrintAndSave(self.format_strings, self.filename)
        if self.save_in_file:
           printsave.save_in_file()
        if self.print_result:
           printsave.print_result()    
