# -*- coding: cp1251 -*-
import PrintAndSave
class Admin():
    "Get and set information about all values that are using in testing"
    
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

    def save_in_db(self, save_in_db = True):
        self.save_in_db = save_in_db
        
    def format_string(self, formats=None):
        self.format_strings = formats

    def set_filename(self, filename):
        self.filename = filename

    def save_results(self, results = None):
        print self.format_strings
        printsave = PrintAndSave.PrintAndSave(self.format_strings, self.filename)
        if self.save_in_file:
           printsave.save_in_file()
        if self.save_in_db:
           printsave.save_in_db()    
