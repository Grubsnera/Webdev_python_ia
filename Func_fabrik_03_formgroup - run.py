""" ****************************************************************************
Script to RUN CREATE Joomla Fabrik form group record
Copyright (C) AB Janse van Rensburg 20190311
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
funcfile.writelog("SCRIPT: FUNC_FABRIK_03_FORMGROUPCREATE_RUN")
funcfile.writelog("------------------------------------------")

# CALL THE FUNCTION
import Func_fabrik_03_formgroup
try:
    i_gr = Func_fabrik_03_formgroup.Fabrik_formgroup()
    print(i_gr)
except Exception as e:
    funcsys.ErrMessage(e)

# CLOSE THE LOG WRITER
funcfile.writelog("Now")
funcfile.writelog("COMPLETED: FUNC_FABRIK_01_FORMGROUPCREATE_RUN")
funcfile.writelog("---------------------------------------------")
