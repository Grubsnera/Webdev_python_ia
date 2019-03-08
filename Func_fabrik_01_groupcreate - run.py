
import sys

# Add own module path
sys.path.append('S:/_my_modules')
sys.path.append('S:/')

import funcfile
import funcmail
import funcsys

funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FUNC_FABRIK_01_GROUPCREATE_RUN")
funcfile.writelog("--------------------------------------")

import Func_fabrik_01_groupcreate

try:
    i_gr = Func_fabrik_01_groupcreate.Fabrik_groupcreate()
    print(i_gr)
except Exception as e:
    funcsys.ErrMessage(e)

# Close the log writer
funcfile.writelog("Now")
funcfile.writelog("COMPLETED: FUNC_FABRIK_01_GROUPCREATE_RUN")
funcfile.writelog("-----------------------------------------")
