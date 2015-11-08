class PrintAndSave():
    def __init__(self, format_strings =None, filename = "test1"):
        self.format_strings = format_strings
        print "!!!!!!!!!!!"
        print self.format_strings
        self.filename = filename

    def save_in_file(self, data = "oops" ):
        fn = open(self.filename,"w")
        if self.format_strings is not None:
            fn.write(self.format_strings)
            print "Saved data in file"
        else:
            fn.write(data)
            print "got nothing"
        

    def print_result(self, data = "oops"):
        print "We should use printer here"
