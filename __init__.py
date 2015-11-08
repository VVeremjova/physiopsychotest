from admin.adminPart import Admin
from admin.FormatResult import FormatResult
if __name__ == "__main__":
    admin = Admin()
    fres = FormatResult()
    formres = fres.fresult()
    print formres
    admin.format_string(formres)
    admin.set_filename("newtest1")
    print "is save"
    admin.save_in_file()
    admin.save_results()
    print ">>>>>>>>>>>>>"
    admin.print_result()
    admin.save_results()
    admin.print_result = False
    print ">>>>>>>>>>>>>"
    admin.save_results()
    print admin.__doc__
    
