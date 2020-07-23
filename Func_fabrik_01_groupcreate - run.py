"""
Script to run CREATE Joomla Fabrik group record
Copyright (C) AB Janse van Rensburg 20190308
"""

# IMPORT SYSTEM OBJECTS

# IMPORT FUNCTIONS
from _my_modules import funcfile
from _my_modules import funcsys

# IMPORT SCRIPT
import Func_fabrik_01_groupcreate

# DECLARE VARIABLES
i_gr: int = 0

# OPEN THE LOG WRITER
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FUNC_FABRIK_01_GROUPCREATE_RUN")
funcfile.writelog("--------------------------------------")

# CALL THE FUNCTION
try:
    # i_gr = Func_fabrik_01_groupcreate.fabrik_groupcreate(True)
    print(i_gr)
except Exception as e:
    funcsys.ErrMessage(e)

# CLOSE THE LOG WRITER
funcfile.writelog("Now")
funcfile.writelog("COMPLETED: FUNC_FABRIK_01_GROUPCREATE_RUN")
funcfile.writelog("-----------------------------------------")
