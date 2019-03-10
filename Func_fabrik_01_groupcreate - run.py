""" ****************************************************************************
Script to RUN CREATE Joomla Fabrik group record
Copyright (C) AB Janse van Rensburg 20190308
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
funcfile.writelog("SCRIPT: FUNC_FABRIK_01_GROUPCREATE_RUN")
funcfile.writelog("--------------------------------------")

# CALL THE FUNCTION
import Func_fabrik_01_groupcreate
try:
    i_gr = Func_fabrik_01_groupcreate.Fabrik_groupcreate("T")
    print(i_gr)
except Exception as e:
    funcsys.ErrMessage(e)

# CLOSE THE LOG WRITER
funcfile.writelog("Now")
funcfile.writelog("COMPLETED: FUNC_FABRIK_01_GROUPCREATE_RUN")
funcfile.writelog("-----------------------------------------")
