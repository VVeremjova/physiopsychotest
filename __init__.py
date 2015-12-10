
def isSQLite3(filename):
    from os.path import isfile

    return isfile(filename)

# Check that db is ready
from admin.saveInDB import SaveInDB
from start import Start
# Will set db_name in config
db_name = "example.db"
db = SaveInDB(db_name);
is_programm_ready= False
# is_programm_ready = isSQLite3(db_name)
if not is_programm_ready:
    # db.createDB();
    is_programm_ready = isSQLite3(db_name)
# db.closeDB()

start_program = Start(None,is_programm_ready, db_name)
