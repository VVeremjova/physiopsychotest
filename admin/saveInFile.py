import ConfigParser


class SaveInFile():
	def __init__(self, arg):
		self.arg = arg
		config = ConfigParser.RawConfigParser()
        config.read('format.ini')
        self.filename=  config.get('Main', 'file_name')
		

	 def save_in_file(self, data = "oops" ):
        fn = open(self.filename,"w")
        
        fn.write(data)
        print "Saved data in file"
