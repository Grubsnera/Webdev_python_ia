""" ****************************************************************************
Script
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
funcfile.writelog("SCRIPT: RECIPY_FABRIK_01_RUNALL")
funcfile.writelog("-----------------------")

# CALL THE GROUP CREATE FUNCTION
import Func_fabrik_01_groupcreate
try:
    i_gr = Func_fabrik_01_groupcreate.fabrik_groupcreate()
    print("Group: "+str(i_gr))
except Exception as e:
    funcsys.ErrMessage(e)

# CALL THE FORM CREATE FUNCTION
import Func_fabrik_02_formcreate
try:
    i_fo = Func_fabrik_02_formcreate.Fabrik_formcreate()
    print("Form: "+str(i_fo))
except Exception as e:
    funcsys.ErrMessage(e)

# CALL THE FORMGROUP CREATE FUNCTION
import Func_fabrik_03_formgroup
try:
    i_fg = Func_fabrik_03_formgroup.Fabrik_formgroup("F",str(i_gr),str(i_fo))
    print("Formgroup: "+str(i_fg))
except Exception as e:
    funcsys.ErrMessage(e)

# CALL THE LIST CREATE FUNCTION
import Func_fabrik_04_listcreate
try:
    i_li = Func_fabrik_04_listcreate.Fabrik_listcreate("F","New LIST to setup",str(i_fo))
    print("List: "+str(i_li))
except Exception as e:
    funcsys.ErrMessage(e)

# CLOSE THE LOG WRITER
funcfile.writelog("Now")
funcfile.writelog("COMPLETED: RECIPY_FABRIK_01_RUNALL")
funcfile.writelog("----------------------------------")
