import sqlite3

class SaveInDB() :
    def __init__(self,filename = 'example.db'):
        db_file = filename
        self.conn = sqlite3.connect(filename)
        

    def createDB(self):
    	# Create table
        c = self.conn.cursor()
    	c.execute('''CREATE TABLE Users
    	             (id_ text, name text, gender text, date_age text, 
                      occupation text, work_experience text,
                      last_work_experience text,
                      comments text)''')

        c.execute('''CREATE TABLE Results
                     (name text, total_errors int, correct_answers int)''')
        self.conn.commit()

    def addNewClient(self,params):
        c = self.conn.cursor()
        c.execute("INSERT INTO Users VALUES (?,?, ?, ?, ?,? ,? , ?)",params)
        # Save (commit) the changes
        self.conn.commit()

    def searchClient(self, user_name):
        params = (user_name,)
        c = self.conn.cursor()        
        curs = c.execute('SELECT * FROM Users WHERE name=?', [user_name])
        res=c.fetchone()
        return res

    def updateClient(self,params):
        # Insert a row of data
        c = self.conn.cursor()
        c.execute("UPDATE Users SET id_ = ?, gender = ?,date_age = ?,occupation =?,work_experience=?,last_work_experience=?, comments = ?    WHERE name = ?;",params)
        self.conn.commit()

    def close(self):
    	# We can also close the connection if we are done with it.
    	# Just be sure any changes have been committed or they will be lost.
    	self.conn.close()

