""" ****************************************************************************
Script to RUN CREATE Joomla Fabrik form record
Copyright (C) AB Janse van Rensburg 20190310
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
funcfile.writelog("SCRIPT: FUNC_FABRIK_02_FORMCREATE_RUN")
funcfile.writelog("--------------------------------------")

# CALL THE FUNCTION
import Func_fabrik_02_formcreate
try:
    i_fo = Func_fabrik_02_formcreate.Fabrik_formcreate("T")
    print(i_fo)
except Exception as e:
    funcsys.ErrMessage(e)

# CLOSE THE LOG WRITER
funcfile.writelog("Now")
funcfile.writelog("COMPLETED: FUNC_FABRIK_02_FORMCREATE_RUN")
funcfile.writelog("-----------------------------------------")
