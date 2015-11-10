from admin.adminPart import Admin
from admin.FormatResult import FormatResult
if __name__ == "__main__":
    admin = Admin()
    fres = FormatResult()
    formres = fres.fresult()
    #print formres
    admin.format_string(formres)
    admin.set_filename("newtest1.txt")
    print "is save"
    admin.print_result = False
    admin.save_in_file()
    admin.save_results()
    #print ">>>>>>>>>>>>>"
    #admin.print_result()
    #admin.save_results()
    #print ">>>>>>>>>>>>>"
    #admin.save_results()
    #print admin.__doc__
    
