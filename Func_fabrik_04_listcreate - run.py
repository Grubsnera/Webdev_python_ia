""" ****************************************************************************
Script to RUN CREATE Joomla Fabrik list record
Copyright (C) AB Janse van Rensburg 20190321
*****************************************************************************"""

# IMPORT SYSTEM OBJECTS
import sys

# ADD OWN MODULE PATH
sys.path.append('S:/_my_modules')

# IMPORT FUNCTIONS
import funcfile
import funcsys

# OPEN THE LOG WRITER
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FUNC_FABRIK_04_LISTCREATE_RUN")
funcfile.writelog("--------------------------------------")

# CALL THE FUNCTION
import Func_fabrik_04_listcreate
try:
    i_li = Func_fabrik_04_listcreate.Fabrik_listcreate("T")
    print(i_li)
except Exception as e:
    funcsys.ErrMessage(e)

# CLOSE THE LOG WRITER
funcfile.writelog("Now")
funcfile.writelog("COMPLETED: FUNC_FABRIK_04_LISTCREATE_RUN")
funcfile.writelog("----------------------------------------")
