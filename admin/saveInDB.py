import sqlite3

class SaveInDB() :
    def __init__(self,filename = 'example.db'):
        db_file = filename
        conn = sqlite3.connect(filename)
        

    def createDB(self):
    	# Create table
        c = self.conn.cursor()
    	c.execute('''CREATE TABLE stocks
    	             (id int, name text, gender text, date_age text, 
                      occupation text, work_experience int,
                      last_work_experience int,
                      comments text)''')
        self.conn.commit()

    def addNewClient(self, id, name, gender, date_age):
        # Insert a row of data
        c = conn.cursor()
    	c.execute("INSERT INTO stocks VALUES (id,name, gender, date_age, "", , , "")")
    	# Save (commit) the changes
    	self.conn.commit()

    def closeDB(self):
    	# We can also close the connection if we are done with it.
    	# Just be sure any changes have been committed or they will be lost.
    	self.conn.close()

